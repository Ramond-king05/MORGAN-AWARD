import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe
#import wkhtmltopdf
#from wkhtmltopdf import WKHtmlToPdf

st.set_page_config(layout="centered", page_icon="🎓", page_title= "Ramond")
st.title("ACTIVE MEMBERS AWARD 🎁")

st.write(
    "This app is created for morgan active members"
 )


left, right = st.columns(2)

right.write("Here's the template we'll be using:")

right.image("certy.png", width=300)




env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
html=("templates.html")
template = env.get_template("templates.html")

left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Member name")

number = form.text_input("Member number")


grade = form.slider("Grade", 1, 100, 60)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        student=student,
        number=number,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )
    
st.balloons()

    

pdf = pdfkit.from_string(html, False)
right.success("🎉 Your diploma was generated!")
st.write(html, unsafe_allow_html=True)
st.write("")
right.download_button(
    "⬇️ Download PDF",
    data=pdf,
    file_name="MORGAN.pdf",
    mime="application/octet-stream",
    )