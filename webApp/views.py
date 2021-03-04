from django.shortcuts import render
from django.http import HttpResponse
import random
import string
from django.template import loader
import hashlib


# Create your views here.
def index(request):
    return render(request, 'index.html')

def details(request):
    return (render(request,'details.html'))


def randomString(request):
    template = loader.get_template('random.html')
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for i in range(16))
    context = {
        'random_string': random_string,
    }
    return HttpResponse(template.render(context, request))


def hasher(request):
    return render(request, 'hasher.html')


def your_hash(request):

    try:
        text = request.POST['Input Text']
        hash = request.POST['hash']
    except(KeyError):

        return (render(request,'details.html',{'error_message':"Some elements are missing for the Hash method!!"}))
    texte_hashe = hasher_fun(text, hash)

    context = {
        'text': text,
        'hash': hash,
        'texte_hashe': texte_hashe,

    }
    return render(request, 'your_hash.html', context)

def ip_address(request):
    return(render(request,'IP_address_checker.html'))

def your_IP(request):
    try:
        ip=request.POST['Input Text']
    except(KeyError):

        return (render(request, 'details.html', {'error_message': "Some elements are missing for the IP Checker method!!"}))
    text=IP_fun(ip)

    return(render(request,'your_IP.html',{'text':text}))













def hasher_fun(text, hash):
    hashvalue = text
    if hash=='md5':
        hashobj = hashlib.md5()
        hashobj.update(hashvalue.encode("utf8"))
    else:
        hashobj = hashlib.sha256()

        hashobj.update(hashvalue.encode("utf8"))

    return(hashobj.hexdigest())


def IP_fun(ip):
    parts = ip.split(".")
    if len(parts) < 4 or len(parts) > 4:
        return "invalid IP length should be 4 not greater or less than 4"
    else:
        while len(parts) == 4:
            a = int(parts[0])
            b = int(parts[1])
            c = int(parts[2])
            d = int(parts[3])
            if a <= 0 or a == 127:
                return "invalid IP address"
            elif d == 0:
                return "host id  should not be 0 or less than zero "
            elif a >= 255:
                return "should not be 255 or greater than 255 or less than 0 A"
            elif b >= 255 or b < 0:
                return "should not be 255 or greater than 255 or less than 0 B"
            elif c >= 255 or c < 0:
                return "should not be 255 or greater than 255 or less than 0 C"
            elif d >= 255 or c < 0:
                return "should not be 255 or greater than 255 or less than 0 D"
            else:
                return "Valid IP address ", ip