class Note:
    def __init__(self, content):
        self.content = content

class Notebook:
    def __init__(self):
        self.notes = []  # Noteのリスト

    def add_note(self, content):
        note = Note(content)
        self.notes.append(note)

    def show_notes(self):
        if not self.notes:
            print("メモはありません。")
            return
        for i, note in enumerate(self.notes):
            print(f"{i}: {note.content}")

    def delete_note(self, index):
        if index < 0 or index >= len(self.notes):
            print("無効なインデックスです。")
            return
        del self.notes[index]
        print(f"メモ {index} を削除しました。")

buylist = Notebook()
buylist.add_note("牛乳")
buylist.add_note("卵")
buylist.add_note("パン")
buylist.show_notes()
buylist.delete_note(1)
buylist.show_notes()