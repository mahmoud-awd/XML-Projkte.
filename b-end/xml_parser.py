import xml.etree.ElementTree as ET
import json
import re

def clean_html(raw_html):
    clean_text = re.sub('<.*?>', '', raw_html)  # Entfernt HTML-Tags
    return clean_text.strip()

def load_xml(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    questions = []
    
    for question in root.findall('question'):
        q_type = question.get('type', 'unknown')
        q_name = question.find('name/text')
        q_text = question.find('questiontext/text')
        
        if q_text is not None and q_name is not None:
            questions.append({
                'type': q_type,
                'name': q_name.text,
                'text': clean_html(q_text.text)
            })
    
    return questions

def filter_questions(questions, q_type=None, keyword=None):
    filtered = questions
    if q_type:
        filtered = [q for q in filtered if q['type'] == q_type]
    if keyword:
        filtered = [q for q in filtered if keyword.lower() in q['text'].lower()]
    return filtered

def save_to_json(data, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    file_path = "data.xml"
    questions = load_xml(file_path)
    
    print("Geladene Fragen:")
    for q in questions:
        print(f"[{q['type']}] {q['name']}: {q['text'][:100]}...")
    
    save_to_json(questions, "questions.json")
    print("Fragen wurden als 'questions.json' gespeichert.")
    
    # Beispiel: Nur Multiple-Choice-Fragen anzeigen
    mc_questions = filter_questions(questions, q_type="multichoice")
    print(f"\nGefilterte Multiple-Choice-Fragen: {len(mc_questions)} gefunden.")
    
    # Beispiel: Fragen mit dem Keyword "PHP" anzeigen
    php_questions = filter_questions(questions, keyword="PHP")
    print(f"\nGefilterte Fragen mit 'PHP': {len(php_questions)} gefunden.")
