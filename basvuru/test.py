import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Streamlit başlığı
st.title("Otomatik İş Başvuru Sistemi")

# Kullanıcıdan bilgiler al
city = st.text_input("Hangi şehirde iş arıyorsunuz?")
degree = st.selectbox("Kaçıncı sınıfsınız?", ["1. Sınıf", "2. Sınıf", "3. Sınıf", "4. Sınıf", "Mezun"])
job_type = st.selectbox("Hangi çalışma türünü istiyorsunuz?", ["Stajyer", "Yarı Zamanlı", "Tam Zamanlı"])
working_days = st.slider("Kaç gün çalışmak istiyorsunuz?", 2, 5, 3)
skills = st.text_area("istediğiniz alan (örn: yazılım, Makine mühendisliği, finans)")

if st.button("İş İlanlarını Tara ve Başvur!"):
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920x1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    url = "https://www.youthall.com/tr/jobs/"
    driver.get(url)
    
    wait = WebDriverWait(driver, 10)
    time.sleep(5)

    # Sayfayı aşağı kaydırarak ilanları yükle
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000);")
        time.sleep(2)

    job_elements = driver.find_elements(By.CLASS_NAME, "l-grid__col.l-grid__col--lg-4.l-grid__col--md-4.l-grid__col--xs-12.u-gap-bottom-25")
    st.write(f"{len(job_elements)} ilan bulundu.")

    applied_jobs = []

    for job in job_elements:
        try:
            job_link = job.find_element(By.TAG_NAME, "a").get_attribute("href")
            driver.execute_script(f"window.open('{job_link}', '_blank');")
            driver.switch_to.window(driver.window_handles[1])
            
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
            job_title = driver.find_element(By.TAG_NAME, "h1").text
            
            try:
                job_description = driver.find_element(By.CLASS_NAME, "c-job_post_content").text.strip()
            except:
                job_description = "İlan açıklaması bulunamadı."
            
            match_score = 0
            if city.lower() in job_description.lower():
                match_score += 25
            if degree.split(" ")[0] in job_description:
                match_score += 25
            if job_type.lower() in job_description.lower():
                match_score += 25
            if any(skill.lower() in job_description.lower() for skill in skills.split(",")):
                match_score += 25
            
            if match_score >= 50:
                try:
                    apply_button = driver.find_element(By.CLASS_NAME, "c-button--primary")
                    apply_button.click()
                    applied_jobs.append((job_title, "Başvuru Yapıldı", match_score))
                except:
                    applied_jobs.append((job_title, "Başvuru Yapılamadı", match_score))
            else:
                applied_jobs.append((job_title, "Başvuru Yapılmadı", match_score))
            
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            time.sleep(2)
        except Exception as e:
            st.write(f"Hata oluştu: {e}")
            break
    
    # Sonuçları göster
    st.subheader("Başvuru Sonuçları")
    for job_title, status, score in applied_jobs:
        st.write(f"**{job_title}** - {status} (%{score})")
    
    driver.quit()
