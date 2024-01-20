from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
from django.views.decorators.cache import never_cache

from filters.vintage import VintageFilter
from filters.grayscale import GrayscaleFilter
from filters.lark import LarkFilter
from filters.sepia import SepiaFilter
from filters.valencia import ValenciaFilter
from filters.clarendon import ClarendonFilter

@never_cache
def home(request):
    if request.method == 'GET' and 'uploaded_image_path' in request.GET:
        button_number = request.GET.get('button_number')
        uploaded_image_path = request.GET.get('uploaded_image_path')

        effect_mapping = {
            "1": VintageFilter.apply_vintage_filter,
            "2": GrayscaleFilter.apply_grayscale_filter,
            "3": LarkFilter.apply_lark_filter,
            "4": SepiaFilter.apply_sepia_filter,
            "5": ValenciaFilter.apply_valencia_filter,
            "6": ClarendonFilter.apply_clarendon_filter,
        }

        if button_number in effect_mapping:
            selected_effect = effect_mapping[button_number]
            processed_image_base64 = selected_effect(uploaded_image_path)
            return JsonResponse({'processed_image_base64': processed_image_base64})
        else:
            return JsonResponse({'error': 'Invalid buttonNumber'})
    
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image = fs.url(filename)
        return render(request, 'home.html', {'uploaded_image': uploaded_image})
    
    return render(request, 'home.html')
