import pytest
from lib.reminder import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Jack")
    reminder.remind_me_to("Eat some lunch")
    result = reminder.remind()
    assert result == "Eat some lunch, Jack"
    reminder.remind_me_to("Get back to work")
    result = reminder.remind()
    assert result == "Eat some lunch, Jack"

def test_list_tasks():
    reminder = Reminder('Jack')
    with pytest.raises(Exception) as e:
        reminder.remind()
    error_message = str(e.value)
    assert error_message == "No reminders set!"
    reminder.remind_me_to("Eat some lunch")
    reminder.remind_me_to("Get back to work")

    result = reminder.list_tasks()
    assert result == ['Eat some lunch', 'Get back to work']