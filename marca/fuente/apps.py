import logo_kit as lk
from owl import *
from shot import shot, HERE
M = f"file://{HERE}/out/marca"
def inl(L, h=None, w=None):
    s = lk.svg(L)
    return s.replace("<svg ", "<svg " + (f'height="{h}" ' if h else "") + (f'width="{w}" ' if w else ""), 1)
def eq(w=40, h=6, gap=6, c=AMB):
    return f'<div style="display:flex;flex-direction:column;gap:{gap}px"><div style="width:{w}px;height:{h}px;border-radius:{h/2}px;background:{c}"></div><div style="width:{w}px;height:{h}px;border-radius:{h/2}px;background:{c}"></div></div>'
CSS = f"""body{{font-family:'Hanken Grotesk';color:{TIN}}} .bg{{width:800px;height:330px;overflow:hidden;position:relative}} .B{{font-family:'Bricolage Grotesque';font-weight:700;letter-spacing:-.5px}} .lab{{font-size:10px;letter-spacing:1.6px;text-transform:uppercase;color:{NIE};font-weight:600}}"""
def page(body): return f"<html><head><style>{CSS}</style></head><body>{body}</body></html>"

# a) perfil de mensajería
a = f'''<div class=bg style="background:#E9E4DA;display:flex;gap:28px;padding:26px 34px;align-items:center">
 <div style="width:300px;height:278px;background:{HUE};border-radius:18px;padding:24px;display:flex;flex-direction:column;align-items:center;gap:10px;box-shadow:0 1px 0 rgba(0,0,0,.06)">
  <img src="{M}/iconos/gc_avatar_1080.png" style="width:104px;height:104px;border-radius:50%">
  <div class=B style="font-size:22px;color:{TIN};margin-top:4px">Gabinete Contable</div>
  <div style="font-size:12px;color:{NIE}">Cuenta de empresa · La Paz, Bolivia</div>
  <div style="font-size:12px;line-height:1.4;color:{TIN};text-align:center;margin-top:4px">Contabilidad y asesoría para empresas. Libros en orden, un responsable que responde.</div>
 </div>
 <div style="flex:1;display:flex;flex-direction:column;gap:12px">
  <div class=lab>Entrega del período</div>
  <div style="background:#fff;border-radius:14px 14px 14px 4px;padding:16px 18px;font-size:13.5px;line-height:1.5;color:{TIN};max-width:400px">Hola, [nombre]. Le comparto los documentos de [período]: [entregables].<br><b>Pendiente:</b> [documento].<br><b>Próximo paso:</b> [acción, responsable y fecha].<br>Soy [responsable]; si alguna cifra requiere explicación, la revisamos con usted.</div>
  <div style="display:flex;align-items:center;gap:10px">{eq(28,5,4)}<span style="font-size:12px;color:{NIE}">Un mensaje, una entrega, un responsable.</span></div>
 </div></div>'''
shot(page(a), "img/app_perfil.png", 800, 330)

# b) tarjeta frente y dorso (90 × 50 mm)
b = f'''<div class=bg style="background:#E9E4DA;display:flex;gap:36px;align-items:center;justify-content:center">
 <div style="width:342px;height:190px;background:{HUE};border-radius:6px;box-shadow:0 10px 24px rgba(20,37,43,.18);display:flex;align-items:center;justify-content:center">{inl(layers(WS,"color"), h=66)}</div>
 <div style="width:342px;height:190px;background:{PET};border-radius:6px;box-shadow:0 10px 24px rgba(20,37,43,.25);padding:22px 24px;display:flex;flex-direction:column;justify-content:space-between;color:{HUE}">
  <div style="display:flex;justify-content:space-between;align-items:flex-start">
   <div><div class=B style="font-size:17px">[Nombre del profesional]</div><div style="font-size:11.5px;opacity:.85;margin-top:3px">[Cargo confirmado]</div></div>
   {inl([(SYM, AMB)], h=40)}
  </div>
  <div style="display:flex;flex-direction:column;gap:8px">{eq(24,4,3)}<div style="font-size:11px;line-height:1.55">[Teléfono] · [Correo corporativo]<br>Gabinete Contable · La Paz, Bolivia</div></div>
 </div></div>'''
shot(page(b), "img/app_tarjeta.png", 800, 330)

# c) documentos: propuesta y resumen de cierre
row = lambda n, t, d: f'''<div style="display:flex;gap:10px;padding:7px 0;border-top:1px solid #DAD6CC"><div style="font-size:8px;font-weight:700;color:{PET};width:18px">{n}</div><div><div style="font-size:8.5px;font-weight:700;color:{TIN}">{t}</div><div style="font-size:7.5px;color:{NIE};margin-top:2px">{d}</div></div></div>'''
c = f'''<div class=bg style="background:#E9E4DA;display:flex;gap:40px;justify-content:center;align-items:center">
 <div style="width:212px;height:300px;background:{PET};box-shadow:0 10px 24px rgba(20,37,43,.25);padding:26px 22px;display:flex;flex-direction:column;justify-content:space-between;color:{HUE}">
  {inl(layers(WS,"negativo"), h=40)}
  <div><div class=lab style="color:#B9C6C9">Propuesta de servicios</div><div class=B style="font-size:22px;line-height:1.08;margin-top:8px">Contabilidad continua para [empresa]</div><div style="margin-top:12px">{eq(26,4,3)}</div></div>
 </div>
 <div style="width:212px;height:300px;background:#FFFFFF;box-shadow:0 10px 24px rgba(20,37,43,.18);padding:22px 22px">
  <div style="display:flex;justify-content:space-between;align-items:center">{inl(layers(WH,"color"), h=16)}<div class=lab style="font-size:7px">v1 · [fecha]</div></div>
  <div class=B style="font-size:16px;color:{PET};margin-top:20px">Resumen de cierre</div>
  <div style="font-size:8px;color:{NIE};margin:4px 0 10px">Empresa: [nombre] · Período: [mes y año]</div>
  {row("01","Entregado","[Libros y documentos incluidos]")}{row("02","Observaciones","[Qué requiere revisión o confirmación]")}{row("03","Próximo paso","[Acción] · [Responsable] · [Fecha]")}
  <div style="margin-top:8px;display:flex;justify-content:space-between;align-items:flex-end"><div style="font-size:7.5px;color:{NIE}">Responsable: [nombre y canal]</div>{eq(22,3,2.5)}</div>
 </div></div>'''
shot(page(c), "img/app_documentos.png", 800, 330)

# d) web + favicon
d = f'''<div class=bg style="background:#E9E4DA;padding:22px 30px 0">
 <div style="background:#DCD6CB;border-radius:10px 10px 0 0;padding:8px 10px 0;display:flex;gap:8px">
  <div style="background:{HUE};border-radius:8px 8px 0 0;padding:7px 12px;display:flex;align-items:center;gap:8px;font-size:11px;color:{TIN}"><img src="{M}/iconos/favicon.svg" style="width:14px">Gabinete Contable | Contabilidad para empresas</div>
 </div>
 <div style="background:{HUE};height:300px;padding:18px 30px">
  <div style="display:flex;justify-content:space-between;align-items:center">{inl(layers(WH,"color"), h=24)}
   <div style="display:flex;gap:22px;align-items:center;font-size:12px;color:{TIN}"><span>Contabilidad</span><span>Servicios</span><span>El gabinete</span><span style="background:{AMB};color:{TIN};font-weight:700;padding:8px 14px;border-radius:6px">Conversemos</span></div></div>
  <div style="display:flex;justify-content:space-between;align-items:center;margin-top:30px">
   <div><div class=B style="font-size:38px;line-height:1.02;color:{PET}">Sus libros en orden.<br>Cada cuenta, explicada.</div>
    <div style="font-size:13px;color:{NIE};margin-top:12px;max-width:380px;line-height:1.45">Contabilidad continua para empresas y negocios, con un responsable que conoce su caso.</div></div>
   <div style="margin-right:20px">{inl(color(P), h=150)}</div></div>
 </div></div>'''
shot(page(d), "img/app_web.png", 800, 330)
