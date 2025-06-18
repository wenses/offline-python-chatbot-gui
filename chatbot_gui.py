from flet import *

from langchain_community.llms import Ollama

model=Ollama(model="gemma2:2b")

def main(page:Page):
	page.title="CyberMaster ChatBot"

	page.theme_mode="Dark"

	page.appbar=AppBar(
		title=Text('CyberMaster ChatBot'),
		center_title=True,
		bgcolor="#0000ff",
		color="white",)

	def submit_action(e):
		q=qinput.value
		status=Text("Typing...")
		lv.controls.append(
			Container(border_radius=20,
				bgcolor="blue",
				padding=25,
				content=Text(qinput.value)))
		qinput.value=""
		lv.controls.append(status)
		page.update()
		result=model.invoke(q)
		result=result.replace("Gemma","The CyberMaster")
		result=result.replace("Google DeepMind","Blixen Tech")
		page.update()
		

		print(result)
		qinput.value=""
		page.update()
		lv.controls.append(
			Container(border_radius=10,
				bgcolor="red",
				padding=25,
				content=Text(result)))
		lv.controls.remove(status)
		page.update()

	lv=ListView(spacing=10,auto_scroll=True)

	mrow=Stack([Container(bgcolor="black",border_radius=20,padding=20),lv],expand=True)
	qinput=TextField(hint_text="Enter Prompt here",expand=True,
		autofocus=True)

	

	sb=ElevatedButton('Submit',on_click=submit_action)

	qcol=Row(
		controls=[qinput,sb])

	page.add(mrow,qcol)

app(target=main)