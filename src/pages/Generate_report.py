import streamlit as st
from matplotlib.backends.backend_pdf import PdfPages
from io import BytesIO
import matplotlib.pyplot as plt

st.title("\ud83e\uddfe Generate Report")

# Ensure we have figures stored
if 'report_figures' in st.session_state and st.session_state['report_figures']:
    pdf_buffer = BytesIO()

    with PdfPages(pdf_buffer) as pdf:
        for fig in st.session_state['report_figures']:
            # Save each Plotly figure to a temporary PNG using kaleido alternative
            img_bytes = fig.to_image(format="png")
            image = plt.imread(BytesIO(img_bytes), format='png')
            fig_, ax = plt.subplots(figsize=(10, 6))
            ax.imshow(image)
            ax.axis('off')
            pdf.savefig(fig_)
            plt.close(fig_)

    st.success("\u2705 PDF Report Generated!")
    st.download_button(
        label="\ud83d\udcc5 Download PDF Report",
        data=pdf_buffer.getvalue(),
        file_name="Data_Insights_Report.pdf",
        mime="application/pdf"
    )
else:
    st.warning("No visualizations available. Please visit the Dashboard page and upload data.")
