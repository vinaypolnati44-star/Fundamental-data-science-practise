from bs4 import BeautifulSoup
import pandas as pd

html_data = """
<table>
<tr><th>Name</th><th>Age</th><th>Marks</th></tr>
<tr><td>Ram</td><td>20</td><td>85</td></tr>
<tr><td>Sita</td><td>19</td><td>90</td></tr>
<tr><td>Ravi</td><td>21</td><td>78</td></tr>
</table>
"""

soup = BeautifulSoup(html_data, 'html.parser')

rows = []
for tr in soup.find_all('tr'):
    cols = [td.text for td in tr.find_all(['td','th'])]
    rows.append(cols)

df = pd.DataFrame(rows[1:], columns=rows[0])
print(df)
