# FILE: main.py (BATCH VERSION - DIRECTORY INPUT/OUTPUT)

import json
import os
from src.outline_extractor import OutlineExtractor

INPUT_DIR = "app/input"
OUTPUT_DIR = "app/output"

def main():
    extractor = OutlineExtractor()

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(INPUT_DIR, filename)
            print(f"📄 Processing: {pdf_path}")
            
            title, headings = extractor.extract_outline(pdf_path)

            if title is None and headings is None:
                print(f"❌ Skipping {filename} due to extraction error.")
                continue

            formatted_outline = [
                {
                    "level": f"H{heading['level']}",
                    "text": heading["text"],
                    "page": heading["page_num"] + 1
                }
                for heading in headings
            ]

            final_output = {
                "title": title,
                "outline": formatted_outline
            }

            base_name = os.path.splitext(filename)[0]
            output_filename = os.path.join(OUTPUT_DIR, f"{base_name}_outline.json")
            
            with open(output_filename, 'w', encoding='utf-8') as f:
                json.dump(final_output, f, indent=4, ensure_ascii=False)

            print(f"✅ Outline saved to: {output_filename}")

if __name__ == "__main__":
    main()
