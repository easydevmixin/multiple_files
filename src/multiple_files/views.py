# views.py
# -*- coding: utf-8 -*-
from django.shortcuts import redirect, render
from django.shortcuts import render_to_response

from .models import Attachment


def add_attachment(request):
    if request.method == "POST":
        parent_id = request.POST['parent_id']
        files = request.FILES.getlist('myfiles')
        for number, a_file in enumerate(files):
            instance = Attachment(
                parent_id=parent_id,
                file_name=a_file.name,
                attachment=a_file
            )
            instance.save()

        request.session['number_of_files'] = number + 1
        return redirect("multiple_files:add_attachment_done")

    return render(request, "multiple_files/add_attachment.html")


def add_attachment_done(request):
    return render_to_response('multiple_files/add_attachment_done.html',
        context={"num_files": request.session["number_of_files"]})
