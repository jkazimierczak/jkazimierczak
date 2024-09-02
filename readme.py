import urllib.parse
from dataclasses import dataclass
from typing import Optional


readme_begin = """Hello! 👋

I am a person, who has explored various fields of IT over the past decade, with a focus on programming for the last 5 years. 
In 2020, I achieved the finalist position in the Technical Innovation Olympiad. 
My experience has led me to take roles of an architect or team lead in university projects.
"""


@dataclass
class Header:
    text: str
    level: int = 4
    prepend_newline: bool = True

    @property
    def markdown(self):
        out = "\n" if self.prepend_newline else ""
        out += f"{'#' * self.level} {self.text}"
        return out


@dataclass
class SimpleIcon:
    label: str
    logo: Optional[str] = None
    logo_base64: Optional[str] = None
    logo_color: Optional[str] = None
    href: Optional[str] = None

    def __post_init__(self):
        if self.logo is None:
            self.logo = self.label.lower()
        if self.logo:
            self.logo = self.logo.replace("#", "")

    @property
    def badge_logo(self):
        if not self.logo_base64:
            return self.logo
        return f"data:image/svg+xml;base64,{self.logo_base64}"

    @property
    def badge(self):
        label = urllib.parse.quote(self.label)
        logo_color = f"&logoColor={self.logo_color}" if self.logo_color else ""
        return f"https://img.shields.io/badge/-{label}-000000?logo={self.badge_logo}&style=flat{logo_color}"

    @property
    def markdown(self):
        if not self.href:
            return f"![{self.label}]({self.badge})"

        return f"[![{self.label}]({self.badge})]({self.href})"


items = [
        Header("Technologies I work with"),
        # Frontend
        Header("Frontend"),
        SimpleIcon("TypeScript"),
        SimpleIcon("Next.js"),
        SimpleIcon("React"),
        SimpleIcon("Vue.js"),
        SimpleIcon("Redux Toolkit", "redux", logo_color="7248b6"),
        SimpleIcon("Tailwind CSS", "tailwindcss"),
        SimpleIcon("React Query / SWR", "react-query"),
        SimpleIcon("GraphQL", "graphql", logo_color="de33a6"),
        SimpleIcon("Figma"),
        # Backend
        Header("Backend"),
        SimpleIcon("NestJS"),
        SimpleIcon("Java", "openjdk"),
        SimpleIcon("Python"),
        SimpleIcon("Drizzle ORM", "drizzle", href="https://orm.drizzle.team/"),
        SimpleIcon(
            "SuperTokens",
            logo_base64="iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAGbElEQVR4AeXBC2zUdwHA8e//d/9ee7RdGV2hUFpUsJSiMkfXFkS2uTF0CgiOJlOHA3FJrSRmTg0JJk2YhBjZFlwFxkMKKAi4QZgZWIZ0Y4Q+6EYdx7OA62jXK30cfV7v7v8zRadHe/fv//73GNjPR5FSMpwJhjnBMCcY5gTDnGCYU4miy3VX09ra2jIqq2qygXQGa09LG2ufmp1VnzpmzOXExAQ3EaYSQYePHP3qc79Y9TqQTAgemv2VrRt+t245EaBIKQm34tVrV+zdf2A94ee1nzmlEkaW4uJiwkVKydT7Z2hn7eefIDJEycYtxRMmpL+T+flJVwkDS3FxMeEy9f4ZElCIsLK3jv+gp7e3YeaM3BpCJAiT7Gn5HqJo2/Zdr7Y7nTZCJAiDvfsPLAIsRNnM2XO7CZEgDIpXr/0LdymVKLDZ4thU8hKTMydhlJSSwhXP8977tejJnpYv7WdOKZikEqLp+Q/b0bH+xbXk5U4nWIqisPGVdfTLmzWHSBGEqKendwo68nKnE6pXXv4NkSKIoOVLnyYcHsz5MnqOlB2bjUmCCJr7+KNEQ/nb7y7AJEEEZaSnEQ3XGxozMUlwl4iJiUFHAiYJ7hIWi4VIEITio2OTuRM0HJ+OSYJQnPx5CXeGREwShKK55lHucoL/F1cOzMAEgVkttRMJ0c2ODgpXPM+eva8RsiMFr2GCillvPrmZECz4zvf4uMlBv5r3zvDS+g1UnCjDNM2digkCs5yXHiEEHzc5GOixbywk2gSfgtJdu/Gno6OTkLR+EE+QBGZc2JlDCBYu+Bb+qKpKSA48dpYgCcwoLzxKCO5JTMSfw4f2EZKepgkESWCGuyuJEFWcKMPX5g0vk5iYQLQJgtV4cjIRUFF5mrCwb15MEATBOvT4cSLg7+XvEBblPy4lCIJgubtSCYPW1jZ81V25hmmS/9E8NoIgCMY/fv91fPS4Ma35Rgvh4vJwu6aKTAwSBOPtojfx0enCNE3TCIqUGLY//wIGqRjVfjGJAdxeTJuSlUnFiTKM6nW5CMRq0TBLYNSfsh0M4NXQ1dLSSjQk29xoktv9edoxDBAY0Xo2Fem1EqTK6hqiIWdMOx6N292ofQQDBEbs/kIjJqxe81vCoanJgZ7Z6a109zFY2ffXMATBUC7v+xx+SMktCpJAvF4v4bCoYAlD6exlsIt/XMkQBEM5UlCHH31ebjnzwyr05M2aw46dezCj3ekkb9YcPF4vQ5EE8IdxFehQ0bM/9yAB3OjkFtUiGUrJpq2UbNpKPyEEkyZ+lpT77iMuLpZP9LpcdHf3cPXaP2lvd2LUrvl2dHU35qJDJRB3ZwxNVfMJQJP818LJzbx+IQUjNE3j4qU6Ll6qIxweSO2gvo1b+jxgVRlsg7Wdwr6R+CEI5NXEPgKQktv8+qErfBq2PHEeX45O/NPcSTiqsvBD4M9f561Bx3Ung1QtrSaaJt7bw8zxTnxJSWD7cs/hh8Cfa2+sRIeUDBIf4+X0siqi4d44D4cW1+JPew+BbUn+kAEEA5UoGjq6XARkUzXsz1aQYPUSKTvm2Xl3yWkC6eglMFdrOi214/EhGExBR2s3Q6p8ppqaZVWMS3ARLqXzzmF/toKcsR0MRaJjz7R6fKhESJyqcfS77/OJWkcCa05OoP5mHL0egVtTGEgokhghsaleFk1u4qe5DZjR3QfxVgxRGWiZI4lto534ITHvS6M72fPts+ipbyMsWrsg3op/GXNL8aEykC3lJkVSod9bzzzH+dJ1/IemQWzG7K2jl5Qvx1dXYzLbxzUAVqJp/t++SPqcD9L5N83lTHDs+to2d2PNYgaKHXWOp2ofJj7NgQ9FSsmQNli70dw2r7S4LD/xxBGI9CpsjOtF81gxob6Nfh5LfEqjt6t5VHI88SOs+FckFQJwfVQxLvZg/nX6fWb+Fr558EcEoGJEYd8INt9z3WKJE+hRLJJCdyxHCtZwed9KgjH6wTfSiyrnMZCjagr7cu34evJUJjpix+c10G9p4yhGpLahQ5FSYliJIimSCkZ4XYKNcV6MKJIKRhwu2MSsF39GwvhO9FS/8BQ5q3ZjgCKlJCgdHyaRmOHEqOoXnqbiVzvwZ8bapTzwy+2EW/v5sYzMasQAlWAlZjgJRs6qneSs2km/nuYkwIotpZlIGpnViEEq0WRLcXKHEQxzgmFOMMwJhrl/AYZcMbpbPb1DAAAAAElFTkSuQmCC",
            href="https://supertokens.com/",
        ),
        SimpleIcon("Spring Boot", "springboot"),
        # Databases
        Header("Databases"),
        SimpleIcon("PostgreSQL"),
        SimpleIcon("SQLite"),
        SimpleIcon("Redis"),
        SimpleIcon("MongoDB"),
        # Testing
        Header("Testing"),
        SimpleIcon("Jest"),
        SimpleIcon("Vitest"),
        SimpleIcon(
            "Playwright",
            logo_base64=r"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",
        ),
        SimpleIcon(
            "Test Containers",
            logo_base64="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",
            href="https://testcontainers.com/",
        ),
        # IaC & DevOps
        Header("IaC & DevOps"),
        SimpleIcon("Linux"),
        SimpleIcon("Terraform"),
        SimpleIcon("Ansible"),
        SimpleIcon("Docker"),
        # Teamwork
        Header("Teamwork"),
        SimpleIcon("Git"),
        SimpleIcon("GitHub"),
        SimpleIcon("Bitbucket", logo_color="2484fc"),
        SimpleIcon("Jira", logo_color="2484fc"),
        SimpleIcon("Linear"),
        SimpleIcon("Confluence", logo_color="2484fc"),
    ]


def main():
    lines = [
        readme_begin,
    ]
    for item in items:
        if isinstance(item, Header) or isinstance(item, SimpleIcon):
            lines.append(item.markdown)
            continue
    lines = "\n".join(lines)

    with open("README.md", "w", encoding="utf-8") as f:
        f.writelines(lines)




if __name__ == '__main__':
    main()
