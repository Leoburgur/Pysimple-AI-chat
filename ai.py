import PySimpleGUI as sg
import google.generativeai as palm
import pyperclip


palm.configure(api_key="AIzaSyCKtydVd__KSOmxJX4wT-Utb9Y6MHFPpjg")

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.25,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}

sg.theme("LightBlue1")

layout = [[sg.Text("PySimple AI Chat")],[sg.InputText()], [sg.Button("Send")]]


window = sg.Window("PySimple AI Chat", layout)    

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == "Quit": break
    
    text_input = values[0]
    
    context = ""
    examples = []
    messages = []
    messages.append(text_input)
    response = palm.chat(
      **defaults,
      context=context,
      examples=examples,
      messages=messages
    )
    
    sg.popup(response.last) # Response of the AI to your most recent request

    pyperclip.copy(response.last)

window.close()
