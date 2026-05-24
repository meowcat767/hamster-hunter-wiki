import json

def define_env(env):

    @env.macro
    def ContraptionCard(name, img, price, automated, desc):
        return f"- ![{name} image](/assets/{img}) **{name}**<br>Price: ${price}<br>Can be automated: {automated}<br>*{desc}*\n"