# report_pdf.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

import pandas as pd
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader

# Save a matplotlib Figure to a BytesIO and return
def fig2BytesIO(fig):
    bfile = BytesIO()
    fig.savefig(bfile, format='png')
    bfile.seek(0)
    return bfile

# Draw Title
def drawTitle(cvs, x, y, width, title):
    cvs.saveState()
    
    # Set font and colors
    cvs.setFont("Helvetica", 24)
    cvs.setFillColorRGB(0, 0, 0.5)
    cvs.setStrokeColorRGB(0, 0, 0.5)
    
    # Draw title
    cvs.drawString(x, y, title)

    # Draw a dark blue line under title
    cvs.line(x, y-10, x+width, y-10)
    
    cvs.restoreState()

# Draw Section title
def drawSectionTitle(cvs, x, y, title):
    cvs.saveState()
    
    # Set font, color and draw title
    cvs.setFont("Helvetica", 14)
    cvs.setFillColorRGB(0, 0, 0.5)
    cvs.drawString(x, y, title)
    
    cvs.restoreState()

# Draw a token list as a paragraph with wrapping
def drawParagraph(cvs, x, y, width, tokens):
    cvs.saveState()                         # Save current state
    cvs.setFont("Helvetica", 12)            # Set font and color
    cvs.setFillColorRGB(0, 0, 0)
    
    to = cvs.beginText(x, y)                # Create a PDFTextObject at (x, y)
    for token in tokens:                    # Render each string token
        currx = to.getX()                   # Get current x-position
        strw = cvs.stringWidth(token)       # Measure next string width
        if currx + strw > x + width:        # If word runs over right boundary 
            to.textLine()                   # ... move to next line
        to.textOut(token + " ")             # Add token text with space.
    cvs.drawText(to)                        # Render all text to Canvas

    cvs.restoreState()                      # Restore saved state

# Utility function to draw a table
def drawTable(cvs, x, y, width, height, lol):
    cvs.saveState()
    
    # Get Metrics
    nrows = len(lol)                        # Number of rows
    ncols = max([len(row) for row in lol])  # Compute number of columns
    cw, ch = width/ncols, height/nrows      # cell width and cell height
    cm = 5                                  # Cell margin
    
    # Draw column titles
    cvs.setFillColorRGB(0.9, 0.9, 0.9)      # Background color
    for c in range(ncols):
        cx, cy = x + c*cw, y-ch             # Coordinates and background
        cvs.rect(cx, cy, cw, ch, stroke=0, fill=1)
    
    cvs.setFont("Helvetica-Bold", 12)       # Font for cells
    cvs.setFillColorRGB(0, 0, 0)            # Text color
    for c in range(ncols):
        title = lol[0][c]                   # Assume first list has titles
        txt = str(title)                    # Column title
        cx, cy = x + c*cw, y-ch             # Coordinates
        cvs.drawString(cx+cm, cy+cm, txt)   # Cell text
    
    # Draw table entries
    cvs.setFont("Helvetica", 12)
    for r in range(1, nrows):               # Rows
        for c in range(ncols):              # Columns
            txt = str(lol[r][c])            # Element
            cx, cy = x + c*cw, y-(r+1)*ch   # Draw entries
            cvs.drawString(cx+cm, cy+cm, txt)

    # Add table grid over top
    Xs = [x+c*cw for c in range(ncols+1)]
    Ys = [y-r*ch for r in range(nrows+1)]
    cvs.grid(Xs, Ys)
    
    cvs.restoreState()

# Draw a matplotlib Figure on a PDF
def drawFigure(cvs, fig, x, y, width):
    bfile = BytesIO()
    fig.savefig(bfile, format='png')        # Save figure image to a BytesIO
    bfile.seek(0)
    ir = ImageReader(bfile)                 # Wrap ImageReader
    cvs.drawImage(ir, x, y, width=width, preserveAspectRatio=True)
    
# Generate report as PDF file
def generate_pdf(fig1, fig2, lol, fname):
    # Get page metrics
    inch = 72                               # Points per inch
    page_w, page_h = (8.5*inch, 11*inch)    # Letter paper size (points)
    mrgn = 50                               # Page margin (points)

    # Create a Canvas object and set page size
    cvs = canvas.Canvas(fname)
    cvs.setPageSize((page_w, page_h))

    # Draw Title and a line
    drawTitle(cvs, mrgn, 710, page_w-2*mrgn, "Screening Report")

    # Draw paragraph
    para   = '''This report summarizes results from all dose-response 
                experiments. Consult assay documentation for detailed 
                experimental procedures.'''
    drawParagraph(cvs, mrgn, 670, page_w-2*mrgn, para.split())

    # Draw first section title
    drawSectionTitle(cvs, mrgn, 610, "Experimental Data Heat Map")

    # Draw heatmap image. Origin is at bottom left.
    drawFigure(cvs, fig1, mrgn+80, 265, 400)

    # Draw second section title
    drawSectionTitle(cvs, mrgn, 315, "Sample IC50s")

    # Draw a table
    drawTable(cvs, 0.5*(page_w-350), 290, 350, 180, lol)

    # Stop writing to current page and begin next page
    cvs.showPage()

    # Draw third section title
    drawSectionTitle(cvs, mrgn, 740, "Model Fits")

    # Draw plots image
    drawFigure(cvs, fig2, mrgn+50, 220, 400)

    # Save to file
    cvs.save()

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
