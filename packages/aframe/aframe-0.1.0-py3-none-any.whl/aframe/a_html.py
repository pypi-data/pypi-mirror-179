class ATag:
    def __init__(self):
        self.tagname: str = str()
        self.parameters: dict = dict()
        self.closing_tag: bool = True
    
    def __str__(self):
        builder = list()
        builder.append(f"<{self.tagname}")
        for param, val in self.parameters.items():
            if val:
                param = param.replace('_', '-')
                if val is True:
                    builder.append(param)
                else:
                    builder.append(f'{param}="{val}"')
        if self.closing_tag:
            builder.append(f"></{self.tagname}>")
        else:
            builder.append('>')
        return ' '.join(builder)

class HTMLBuilder:
    def __init__(self):
        self.scripts: list = list()
        self.scene = None
        self.assets: list = list()
        self.objects: list = list()
        self.configuration: dict = dict()
    
    def build(self):
        def t(i):
            return "\t" * i
        
        html_builder = list()
        html_builder.append('<!DOCTYPE html>\n<html>\n\t<head>')
        for script in self.scripts:
            html_builder.append(f'\n{t(2)}{script}')
        html_builder.append('\n\t</head>\n\t<body>\n')

        if not self.scene:
            self.scene = '<a-scene>'
        html_builder.append(f'{t(2)}{self.scene}\n')

        if self.assets:
            timeout = self.configuration.get('asset_load_timeout', 7000)
            html_builder.append(f'{t(3)}<a-assets timeout="{timeout}">\n')
            for asset in self.assets:
                html_builder.append(f'{t(4)}{asset}\n')
            html_builder.append(f'{t(3)}</a-assets>\n\n')

        for obj in self.objects:
            html_builder.append(f"{t(3)}{obj}\n")
        
        html_builder.append(f'{t(2)}</a-scene>')
        html_builder.append('\n\t</body>\n</html>')
        return ''.join(html_builder)