from django.shortcuts import render
from django.contrib.messages import get_messages

from messages_frame.forms_messages import UserRegistration
from django.contrib import messages

from logging import *
import logging


def logger_method():
    logger = getLogger(__name__)
    # logger.setLevel(DEBUG)

    formatter = Formatter('%(levelname)s:%(name)s:%(message)s')

    file_handler = FileHandler('sample.log')
    file_handler.setLevel(ERROR)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    stream_handler = StreamHandler()
    logger.addHandler(stream_handler)
    stream_handler.setFormatter(formatter)

    logger.error('Something went wrong!')


def message_display(request):

    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()

            logger_method()

            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'You have signed up successfully.')
            # messages.add_message(request, messages.DEBUG, 'You are signed up successfully.')
            messages.info(request, 'Now you can log in')
            messages.error(request, 'Its an error.')

            level = messages.get_level(request)
            print("level", level)

            storage = get_messages(request)
            for message in storage:
                print(message)

    else:
        form = UserRegistration()
    return render(request, 'messages.html', {'forms': form})
