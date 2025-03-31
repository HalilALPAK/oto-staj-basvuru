from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Tarayıcıyı başlat
options = Options()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920x1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Youthall iş ilanları sayfası
url = "https://www.youthall.com/tr/jobs/"
driver.get(url)

wait = WebDriverWait(driver, 10)
time.sleep(5)

# Sayfayı aşağı kaydırarak tüm ilanları yükle
for _ in range(5):  # 5 kez kaydır
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

# İlanları bul
job_elements = driver.find_elements(By.CLASS_NAME, "l-grid__col.l-grid__col--lg-4.l-grid__col--md-4.l-grid__col--xs-12.u-gap-bottom-25")

print(f"{len(job_elements)} ilan bulundu.\n")

index = 0
while index < len(job_elements):
    try:
        job_elements = driver.find_elements(By.CLASS_NAME, "l-grid__col.l-grid__col--lg-4.l-grid__col--md-4.l-grid__col--xs-12.u-gap-bottom-25")  # Yeniden bul

        job = job_elements[index]
        job_link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

        driver.execute_script(f"window.open('{job_link}', '_blank');")
        driver.switch_to.window(driver.window_handles[1])

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

        # İlan Başlığı
        job_title = driver.find_element(By.TAG_NAME, "h1").text

        # İş Açıklaması (c-job_post_content)
        try:
            job_description = driver.find_element(By.CLASS_NAME, "c-job_post_content").text.strip()
        except:
            job_description = "İlan açıklaması bulunamadı."

        # Çıktıyı ekrana yazdır
        print(f"📌 İlan Başlığı: {job_title}\n")
        print(f"📄 İş Açıklaması:\n{job_description}\n")
        print("-" * 80)

        # Sekmeyi kapatıp ana sayfaya dön
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

        time.sleep(3)
        index += 1
    except Exception as e:
        print("Hata oluştu:", e)
        break

print("✅ Tüm ilanlar işlendi, döngüden çıkılıyor.")
driver.quit()
