from phml import PHMLCore

from phml.core.file_types import PHML, JSON, HTML, Markdown
from phml.utils import inspect

if __name__ == "__main__":
    core = PHMLCore()

    (
        core.load("phml/sample1.phml")
        .write("output/out1_as_phml.phml", PHML)
        .write("output/out1_as_json.json", JSON)
        .write("output/out1_as_html.html", HTML)
    )

    (
        core.load("phml/sample2.phml")
        .write("output/out2_as_phml.phml", PHML)
        .write("output/out2_as_json.json", JSON)
        .write("output/out2_as_html.html", HTML)
    )

    print(
        inspect(
            core.load("phml/sample.phml")
            .write("output/sample.pehl")
            .write("output/sample.json", JSON)
            .ast
        )
    )
