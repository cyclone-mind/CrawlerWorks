from DrissionPage import ChromiumPage, ChromiumOptions
from loguru import logger
co = ChromiumOptions()
cp = ChromiumPage(co)
cp.get("https://www.itjuzi.com/ipo", retry=3, interval=2, timeout=15)

detail_links_all = []
for tr in cp.eles("css:.el-table__row"):
    tds = [td.text.strip() for td in tr.eles("x:.//td")[1:]]
    company = tr.ele("tag:a").text
    a_href = tr.ele("tag:a").attr("href")
    detail_links_all.append(a_href)
    logger.info(f"list_page_company is {company} , a_href is {a_href}")
logger.success(f">>>>>total_detail_urls is : {len(detail_links_all)}")
cp.quit()
