# 필요한 라이브러리를 불러옵니다.
from notion_client import Client
import markdownify

# Notion API 키와 페이지 ID를 환경변수에서 불러옵니다.
import os
notion_api_key = os.getenv('NOTION_API_KEY')
notion_page_id = os.getenv('NOTION_PAGE_ID')

# Notion 클라이언트를 초기화합니다.
notion = Client(auth=notion_api_key)

# Notion 페이지의 내용을 가져옵니다.
page_content = notion.pages.retrieve(notion_page_id)

# 페이지의 텍스트 블록만 필터링하여 마크다운 형식으로 변환합니다.
markdown_text = ""
for block in page_content['results']:
    if block['type'] == 'text':
        text_content = block['text']['content']
        markdown_text += markdownify.markdownify(text_content)

# 마크다운 파일을 생성합니다.
with open(f'_posts/{notion_page_id}.md', 'w') as md_file:
    md_file.write(markdown_text)

