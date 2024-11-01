# report_pdf.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import pandas as pd
from io import BytesIO
from reportlab.platypus import *
from reportlab.lib.styles import getSampleStyleSheet

# Save a matplotlib Figure to a BytesIO and return
def fig2BytesIO(fig):
    bfile = BytesIO()
    fig.savefig(bfile, format='png')
    bfile.seek(0)
    return bfile

# Generate report as PDF file
def generate_pdf(fig1, fig2, lol, fname):
    inch   = 72                             # Points per inch
    parts = []                              # Parts of the report
    
    # Initialize simple document template
    doc = SimpleDocTemplate(fname,
                            page_size   = (8.5*inch, 11*inch),
                            bottomMargin= 0.5*inch,
                            topMargin   = 0.5*inch,
                            rightMargin = 1.0*inch,
                            leftMargin  = 1.0*inch)
    
    # Get a sample style sheet and copy styles
    # Includes: Normal, BodyText, Italic, Heading1 ... Heading6, Title, Bullet, Definition, Code
    styles = getSampleStyleSheet()
    N, H1, H2 = styles['Normal'], styles['Heading1'], styles['Heading2']
    
    # Report title with line and space
    parts.append( Paragraph("Screening Report", style=H1) )
    parts.append( Paragraph("_"*78, style=N) )
    parts.append( Spacer(1, 12) )            # width=1, height=12
    
    # Introductory Paragraph
    text = '''This report summarizes results from all dose-response 
              experiments. Consult assay documentation for detailed 
              experimental procedures.'''    
    parts.append( Paragraph(text, style=N) )
    parts.append( Spacer(1, 12))
    
    # Section Title
    parts.append( Paragraph("Experimental Data Heat Map", style=H2) )
    
    # Heatmap Figure
    w, h = fig1.get_figwidth()*inch, fig1.get_figheight()*inch
    parts.append( Image(fig2BytesIO(fig1), width=w, height=h) )
    
    # Section Title
    parts.append( Paragraph("Sample IC50s", style=H2) )
    
    # IC50 Table
    parts.append( Table([lol[0]]) )         # Table header and body
    parts.append( Table(lol[1:], style=tables.LIST_STYLE ) )
    
    parts.append(PageBreak())               # New page
    
    # Model Fit Parameters Section
    parts.append( Paragraph("Model Fits", style=H2) )
    
    # Fits Figure
    w, h = fig2.get_figwidth()*inch, fig2.get_figheight()*inch
    parts.append( Image(fig2BytesIO(fig2), width=w, height=h) )
    
    # Build PDF
    doc.build(parts)

# Test
if __name__ == '__main__':
    from report_utils import *

    # Read data and transpose so columns hold data for single samples
    df = pd.read_csv("data_plate.csv", header=None)
    df = df.transpose()
    
    # Generate heatmap Figure from data
    fig1 = plot_heatmap(df, "Experimental Data")

    # Fit all data to four-parameter logistic model
    guess  = [0, 2, -5, 1]                            # Parameter guesses
    bounds = [[0,0,-9,0], [1,1000,0,1]]               # Parameter bounds
    concs  = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0]  # log(concentrations)
    param_sets = fit_4PLs(df, concs, guess, bounds)   # Fit all data

    # Create a plot showing all data on eight axes.
    fig2 = plot_fits(df, concs, param_sets=param_sets)
    
    # Collect table data as list of lists
    IC50s = [f'{pow(10, float(pset[2])):0.3E}' for pset in param_sets]
    lol   = [ (f'Sample {i+1}', IC50s[i]) for i in range(len(IC50s)) ]
    lol.insert(0, ["Sample ID", "IC50 [M]"])          # Add column headers
    
    # Generate report PDF document
    generate_pdf(fig1, fig2, lol, 'report.pdf')

