import streamlit as st
from gemini_utils import generate_recipe
from recipe_pdf import create_pdf
from io import BytesIO



st.set_page_config(page_title="  🧑‍🍳Introducting RasoiGPT | Your Own AI Chef")

st.title("RasoiGPT:Your Own AI Chef")
st.markdown("Enter ingredients you have,and get a complete recipe with steps!")


col1,col2=st.columns(2)
with col1:
  st.image("https://plus.unsplash.com/premium_photo-1669557211332-9328425b6f39?q=80&w=1974&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
with col2:
  st.image("https://images.unsplash.com/photo-1552611052-33e04de081de?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Rm9vZCUyMGltYWdlc3xlbnwwfHwwfHx8MA%3D%3D")

ingredients=st.text_area("Enter the ingredients you have")

if st.button("Generate Recipe"):
  with st.spinner("Cooking up something delicious....."):
    recipe=generate_recipe(ingredients)
    st.subheader(" 🍽️ Recipe:" + recipe['title'])
    st.write("### Ingredients:")
    st.write(recipe['ingredients'])
    st.write("### Steps:")
    st.write(recipe['steps'])

    pdf_creator=create_pdf(recipe)
    st.download_button(label="📥 Download Recipe as PDF",data=pdf_creator,file_name=f"{recipe['title'].replace(' ','_')}.pdf",mime="application/pdf")


