from __future__ import annotations

from typeguard import typechecked

from relational_algebra import *
from excmanager.Task import SubTask
from jinja2 import Environment, FileSystemLoader

from pathlib import Path


@typechecked
def generate_exercise(
    subtask: SubTask,
    description: str,
    algebra_expression: Operator,
    *,
    correct_attributes_score_perc: float = 0.1,
) -> dict[str, str]:
    """
    Generate an exercise for the given subtask.

    Parameters
    ----------
    subtask : SubTask
        The subtask to generate the exercise for.
    description : str
        The description of the exercise.
    algebra_expression : Operator
        The relational algebra expression to use in the exercise.
    correct_attributes_score_perc : float, optional
        The percentage of the score that is given for correct attributes, by default 0.1
    """
    # create the data for jinja2
    data = dict()
    # subtask - view https://github.com/rwth-acis/dbis-exercise-manager
    task_num = subtask.task.task
    if "." in task_num:
        task_num = task_num.split(".")[0]
    data["subtask"] = {
        "task": {
            "task": task_num,
        },
        "subtask": subtask.subtask,
        "points": subtask.points,
    }
    # description
    data["description"] = description
    # relational algebra expression
    data["correct_solution"] = _generate_relational_algebra_expression_code(
        algebra_expression
    )
    # correct_attributes_score_perc
    data["correct_attributes_score_perc"] = correct_attributes_score_perc

    # load the templates from resources / templates
    abs_path = Path(__file__).parent.resolve() / "resources/templates"
    abs_path = str(abs_path)
    env = Environment(loader=FileSystemLoader(abs_path))
    # render the templates
    # title.md.jinja2
    title_md = env.get_template("title.md.jinja2").render(data)
    # task.md.jinja2
    task_md = env.get_template("task.md.jinja2").render(data)
    # submission.py.jinja2
    submission_py = env.get_template("submission.py.jinja2").render(data)
    # solution.py.jinja2
    solution_py = env.get_template("solution.py.jinja2").render(data)

    # return the rendered templates
    return {
        "title.md": title_md,
        "task.md": task_md,
        "submission.py": submission_py,
        "solution.py": solution_py,
    }


@typechecked
def _generate_relational_algebra_expression_code(
    algebra_expression: Operator,
) -> str:
    """
    Generate a relational algebra expression as a string (python code).

    Parameters
    ----------
    algebra_expression : Operator
        The relational algebra expression to generate the string for.

    Returns
    -------
    str
        The relational algebra expression as a string (python code).
    """
    match algebra_expression:
        case CrossProduct():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"CrossProduct({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case Difference():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"Difference({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case Division():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"Division({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case Intersection():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"Intersection({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case LeftSemiJoin():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"LeftSemiJoin({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case NaturalJoin():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"NaturalJoin({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case Projection(attributes=attributes):
            child = algebra_expression.children[0]
            assert isinstance(attributes, tuple | list)
            # convert attributes to python code str
            a = "("
            a += ", ".join([f"'{attribute}'" for attribute in attributes])
            a += ")"
            return f"Projection({_generate_relational_algebra_expression_code(child)}, {a})"
        case Relation(name=name):
            return f"Relation('{name}')"
        case Rename(mapping=mapping):
            child = algebra_expression.children[0]
            if isinstance(mapping, dict):
                # convert mapping to python code str
                m = "{"
                m += ", ".join(
                    [f"'{key}': '{value}'" for key, value in mapping.items()]
                )
                m += "}"
                return f"Rename({_generate_relational_algebra_expression_code(child)}, {m})"
            elif isinstance(mapping, str):
                return f"Rename({_generate_relational_algebra_expression_code(child)}, '{mapping}')"
            else:
                raise Exception("Fatal Error: mapping is neither a dict nor a str")
        case RightSemiJoin():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"RightSemiJoin({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case Selection(condition=condition):
            child = algebra_expression.children[0]
            assert isinstance(condition, Formula)
            return f"Selection({_generate_relational_algebra_expression_code(child)}, {_generate_relational_algebra_formula_code(condition)})"
        case ThetaJoin(formula=formula):
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            assert isinstance(formula, Formula)
            return f"ThetaJoin({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)}, {_generate_relational_algebra_formula_code(formula)})"
        case Union():
            left_child = algebra_expression.children[0]
            right_child = algebra_expression.children[1]
            return f"Union({_generate_relational_algebra_expression_code(left_child)}, {_generate_relational_algebra_expression_code(right_child)})"
        case _:
            raise Exception(
                f"Fatal Error: Unknown Operator ({repr(algebra_expression)}). Type {type(algebra_expression)} is not supported."
            )


@typechecked
def _generate_relational_algebra_formula_code(algebra_formula: Formula) -> str:
    """
    Generate a relational algebra formula as a string (python code).

    Parameters
    ----------
    algebra_formula : Formula
        The relational algebra formula to generate the string for.

    Returns
    -------
    str
        The relational algebra formula as a string (python code).
    """
    match algebra_formula:
        case Equals(left=left, right=right):
            if isinstance(left, str):
                left = f"'{left}'"
            if isinstance(right, str):
                right = f"'{right}'"
            return f"Equals({left}, {right})"
        case GreaterThan(left=left, right=right):
            if isinstance(left, str):
                left = f"'{left}'"
            if isinstance(right, str):
                right = f"'{right}'"
            return f"GreaterThan({left}, {right})"
        case GreaterEquals(left=left, right=right):
            if isinstance(left, str):
                left = f"'{left}'"
            if isinstance(right, str):
                right = f"'{right}'"
            return f"GreaterEquals({left}, {right})"
        case LessThan(left=left, right=right):
            if isinstance(left, str):
                left = f"'{left}'"
            if isinstance(right, str):
                right = f"'{right}'"
            return f"LessThan({left}, {right})"
        case LessEquals(left=left, right=right):
            if isinstance(left, str):
                left = f"'{left}'"
            if isinstance(right, str):
                right = f"'{right}'"
            return f"LessEquals({left}, {right})"
        case And():
            left_child = algebra_formula.children[0]
            right_child = algebra_formula.children[1]
            return f"And({_generate_relational_algebra_formula_code(left_child)}, {_generate_relational_algebra_formula_code(right_child)})"
        case Not():
            child = algebra_formula.children[0]
            return f"Not({_generate_relational_algebra_formula_code(child)})"
        case Or():
            left_child = algebra_formula.children[0]
            right_child = algebra_formula.children[1]
            return f"Or({_generate_relational_algebra_formula_code(left_child)}, {_generate_relational_algebra_formula_code(right_child)})"
        case _:
            raise Exception(
                f"Fatal Error: Unknown Formula ({repr(algebra_formula)}). Type {type(algebra_formula)} is not supported."
            )
