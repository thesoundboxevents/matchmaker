from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ChatGPT_Integration.chatgpt_client import ChatGPTClient

@csrf_exempt  # Temporarily disable CSRF for testing
def send_to_chatgpt(request):
    if request.method == 'POST':
        text_data = request.POST.get('text_data', '')
        
        # Here you can add any data cleaning or formatting logic
        formatted_data = text_data  # Example, replace with actual formatting logic

        client = ChatGPTClient()
        messages = [{"role": "user", "content": formatted_data}]
        response = client.get_response(messages)

        if response:
            return JsonResponse(response)
        else:
            return JsonResponse({'error': 'No response received from ChatGPT'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)
