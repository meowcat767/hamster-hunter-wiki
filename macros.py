import json

def define_env(env):

    @env.macro
    def ContraptionCard(name, img, price, automated, desc):
        return f"- ![{name} image](/assets/{img}) **{name}**<br>Price: ${price}<br>Can be automated: {automated}<br>*{desc}*"

    @env.macro
    def SpecialContraptionCard(name, img, location, desc):
        return f"- ![{name} image](/assets/{img}) **{name}**<br>Location: {location}<br>*{desc}*"

    @env.macro
    def TurretCard(name, img, price, range, reload, desc):
        return f"- ![{name} image](/assets/{img}) **{name}**<br>Price: ${price}<br>Range: {range}<br>Reload Time: {reload}<br>*{desc}*"