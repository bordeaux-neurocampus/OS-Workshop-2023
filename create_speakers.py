import yaml
import shutil
import pathlib


_FRONTMATTER = """---
name: {}
link: {}
org: {}
img: {}
status: {}
---
"""


if __name__ == "__main__":
    
    shutil.rmtree("_speakers/")
    
    pathlib.Path("_speakers").mkdir(exist_ok=True)
    
    speakers = []
    with open("_data/speakers.yml", "r+") as fp:
        speakers = yaml.load(fp)
        
    for speaker in speakers:
        frontmatter = _FRONTMATTER.format(
            speaker["name"],
            speaker["link"], 
            speaker["org"],
            speaker["img"], 
            speaker["status"]
        )
        
        content = f"""
# {speaker["name"]}

#### {speaker["org"]}

[Go to personal website]({speaker["link"]})

{speaker["bio"]}

        """
        
        filename = "-".join(speaker["name"].split(" ")).lower() + ".md"
        
        with open(f"_speakers/{filename}", "w+") as fp:
            fp.write(frontmatter + content)
            print("Created file: ", f"_speakers/{filename}")