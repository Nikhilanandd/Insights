import streamlit as st
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

st.title("🧾 Generate Report")

if 'report_images' in st.session_state and st.session_state['report_images']:
    pdf_buffer = BytesIO()

    with PdfPages(pdf_buffer) as pdf:
        for img_data in st.session_state['report_images']:
            image = Image.open(BytesIO(img_data)).convert("RGB")
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(image)
            ax.axis('off')
            pdf.savefig(fig)
            plt.close(fig)

    st.success("✅ PDF Report Generated!")
    st.download_button(
        label="📥 Download PDF Report",
        data=pdf_buffer.getvalue(),
        file_name="Data_Insights_Report.pdf",
        mime="application/pdf"
    )
else:
    st.warning("No visualizations available. Go to the Dashboard page and upload data.")
