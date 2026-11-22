from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

html = """
<html>
<body>
    <h2>Student Records</h2>

    <table border="1">
        <tr>
            <td>Ali</td>
            <td>20</td>
            <td>Karachi</td>
        </tr>

        <tr>
            <td>Sara</td>
            <td>21</td>
            <td>Lahore</td>
        </tr>

        <tr>
            <td>Ahmed</td>
            <td>22</td>
            <td>Islamabad</td>
        </tr>
    </table>

</body>
</html>
"""

driver.get("data:text/html;charset=utf-8," + html)
time.sleep(5)

cell = driver.find_element(By.XPATH, "//tr[3]/td[2]")

print("Located Cell Text:", cell.text)

driver.quit()
