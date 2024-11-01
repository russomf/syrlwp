# lorem_ipsum.py
# Streamlining Your Research Laboratory with Python
# Authors:   Mark F. Russo, Ph.D and William Neil 
# Publisher: John Wiley & Sons, Inc.
# License:   MIT (https://opensource.org/licenses/MIT)

from reportlab.pdfgen import canvas

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

if __name__ == '__main__':
    para = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi 
ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla 
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa 
qui officia deserunt mollit anim id est laborum.'''

    cvs = canvas.Canvas("lorem_ipsum.pdf")
    cvs.setPageSize((612, 792))
    
    tokens = para.split()
    drawParagraph(cvs, 50, 742, 200, tokens)
    cvs.save()
