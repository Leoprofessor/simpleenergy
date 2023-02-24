
#escopo do projeto
# https://simpleenergy.com.br/teste/
# 321465 e 98465 ti@simpleenergy.com.br

from audioop import reverse
from datetime import datetime
import pathlib
from sys import displayhook
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib.auth.decorators import login_required
from .models import Referencia
import pandas as pd
import sweetviz as sv
import csv
import PyPDF2
from tika import parser 
import sys,os



def leitor(request):

    if request.method == "GET":
        return render(request, 'leitor.html')
    
    if request.method == "POST":
 
        file = request.FILES.get('file')
        codigo  = request.POST.get('codigo')



        if not file or len(codigo.strip()) == 0:

            messages.add_message(request, constants.ERROR, 'Preencha todos os campos')
            return redirect('/ia/leitor')        


        elif codigo == '98465' or codigo == '321465' :

            if file.name == 'arquivo.txt' or file.name == 'arquivo.pdf':

                ref = Referencia.objects.create(codigo=codigo, arquivo_ia=file)
                ref.save()

                messages.add_message(request, constants.SUCCESS, 'Dados inseridos com sucesso')
                return redirect('/ia/encontrar_codigo')
            
            elif codigo == '321465':
                 
                 if file.name == 'arquivo2.txt' or file.name == 'arquivo2.pdf':
                     
                     ref = Referencia.objects.create(codigo=codigo, arquivo_ia=file)
                     ref.save()

                     messages.add_message(request, constants.SUCCESS, 'Dados inseridos com sucesso')
                     return redirect('/ia/encontrar_codigo')
                 else:
                     messages.add_message(request, constants.ERROR, 'Os arquivos não correspondem ao código')
                     return redirect('/ia/leitor')
            else:
                         
                 
                 messages.add_message(request, constants.ERROR, 'Os arquivos não correspondem ao código')
                 return redirect('/ia/leitor') 

        
        else:

            messages.add_message(request, constants.ERROR, 'Código inexistente')
            return redirect('/ia/leitor')
        

def encontrar_codigo(request):

    if request.method == "GET":
        leitor = Referencia.objects.all()
        return render(request, 'encontrar_codigo.html', {'leitor': leitor})
    

    
def gerar_ia(request, id):

    file = Referencia.objects.get(id=id)
    file = file.arquivo_ia
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    # filename = pathlib.PurePath(fileDir, file.name + suffix)
    filename = os.path.join(fileDir, 'media/')
    fileverdadeiro = filename + str(file)

    if file.name == 'arquivo.pdf' or file.name == 'arquivo2.pdf':
        
        pdf_file = open(fileverdadeiro, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        page = read_pdf.getPage(0)

        hash_security = page.extractText()
        


    elif file.name == 'arquivo.txt' or file.name == 'arquivo2.txt':

        txt_file = open(fileverdadeiro, 'r')
        hash_security = txt_file.read()
    




    return render(request, 'hash.html', {'hash_security': hash_security})


def hash(request):
    return request