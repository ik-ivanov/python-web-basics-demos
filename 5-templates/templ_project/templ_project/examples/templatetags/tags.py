from django import template

register = template.Library()

@register.simple_tag
def show_student_info(student):
    # Student.object.get(student.id).courses.length

    return f"Name is: {student.name}, Age: {student.age}"

@register.simple_tag
def show_student_names(*args, **kwargs):
    return ", ".join([student.name for student in args])


@register.inclusion_tag(
    'examples/tags/student_info.html',
    name='fancy_student',
    takes_context=True
)
def inclusion_student_info(context, student):
    inner_context = {
        'student': student,
        'score': context["random_int"]
    }
    return inner_context
