from .models import (
    Role,
    User,
    Event,
    Question,
    Cutaway,
    Speech,
)


def check_user(user_id):
    user = User.objects.get(tg_id=user_id)
    user_survey = {
        'id': user.tg_id,
        'status': user.role.role,
    }
    return user_survey


def get_db_schedule():
    event = Event.objects.first()
    return event.speeches.all()


def create_cutaway(user_id, user_data):
    user = User.objects.get(tg_id=user_id)
    Cutaway.objects.get_or_create(
        user=user,
        defaults={
            'first_name': user_data['first_name'],
            'last_name': user_data['last_name'],
            'age': user_data['age'],
            'specialization': user_data['job'],
            'stack': user_data['stack'],
            'hobby': user_data['hobby'],
            'objective': user_data['purpose'],
            'location': user_data['region'],
            'grade': user_data['grade'],
        }
    )


def get_random_user():
    return User.objects.order_by('?').first()


def get_question():
    return Question.objects.order_by('?').first()


def delete_question(id):
    Question.objects.filter(id=id).delete()

