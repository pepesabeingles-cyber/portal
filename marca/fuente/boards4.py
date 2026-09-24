import sys, logo_kit as lk
from sereno import *
from shot import shot, HERE
M = f"file://{HERE}/out5/marca"
Wb, Hb = 1600, 900
def inl(L, h=None, w=None):
    s = lk.svg(L); a = (f'height="{h}" ' if h else "") + (f'width="{w}" ' if w else "")
    return s.replace("<svg ", f"<svg {a}", 1)
CSS = f"""body{{font-family:'Jost';color:{TIN}}} .b{{width:{Wb}px;height:{Hb}px;position:relative;overflow:hidden}}
.lab{{font-family:'Jost';font-weight:500;font-size:13px;letter-spacing:3.5px;text-transform:uppercase}}
.serif{{font-family:'Bodoni Moda';font-optical-sizing:auto}}"""
def page(body): return f"<html><head><style>{CSS}</style></head><body>{body}</body></html>"
def tag(txt, c=NIE, x=64, y=48): return f'<div class=lab style="position:absolute;left:{x}px;top:{y}px;color:{c}">{txt}</div>'
only = set(sys.argv[1:]); want = lambda k: not only or k in only

# 1 · logo
if want("logo"):
    b = f'''<div class=b style="background:{HUE};display:flex;align-items:center;justify-content:center">{inl(layers(WV,"color"), w=860)}
    {tag("Gabinete Contable · Identidad")}{tag("01", x=1510)}</div>'''
    shot(page(b), "board/01_logo.png", Wb, Hb)

# 2 · idea
if want("idea"):
    logo = inl(layers(WV, "color"), w=540)
    L = lambda x1, y, x2: f'<div style="position:absolute;left:{min(x1,x2)}px;top:{y}px;width:{abs(x2-x1)}px;height:1px;background:{NIE}"></div>'
    lab = lambda x, y, t: f'<div class=lab style="position:absolute;left:{x}px;top:{y-8}px;width:280px;color:{TIN}">{t}</div>'
    ox, oy = 90, 330
    # posiciones reales del logo a escala
    b = lk.bounds(lk.union(V_TEXT, V_ACC)); sc = 540 / (b[2] - b[0])
    yl = lambda v: oy + (v - b[1]) * sc
    eb = lk.bounds(V_ACC)
    ann = (L(ox + 550, yl((eb[1] + eb[3]) / 2), ox + 590) + lab(ox + 602, yl((eb[1] + eb[3]) / 2), "Filete y ojos · el acento")
           + L(ox + 550, yl(lk.bounds(V_TEXT)[1] + 35), ox + 590) + lab(ox + 602, yl(lk.bounds(V_TEXT)[1] + 35), "El nombre · manda")
           + L(ox + 550, yl(lk.bounds(V_TEXT)[3] - 35), ox + 590) + lab(ox + 602, yl(lk.bounds(V_TEXT)[3] - 35), "Bodoni · sobriedad"))
    txt = f'''<div style="position:absolute;left:1030px;top:290px;width:490px;display:flex;flex-direction:column;gap:24px">
      <div class=serif style="font-size:50px;font-weight:500;line-height:1.08;color:{PET}">El nombre primero.</div>
      <div style="font-size:20px;line-height:1.55">La marca es el nombre: Gabinete Contable en Bodoni, en mayúsculas espaciadas. Sobrio y con autoridad, sin adornos que distraigan.</div>
      <div style="font-size:20px;line-height:1.55">El búho acompaña. Sus ojos, en calma, están entre las dos palabras, sobre la raya que en el libro contable separa y cierra las cuentas. Está presente sin pedir atención.</div>
      <div style="width:80px;height:2px;background:{ORO}"></div>
      <div style="font-size:16px;line-height:1.5;color:{NIE}">La raya y los ojos son el único acento de la marca. En negativo van en oro.</div></div>'''
    bb = f'<div class=b style="background:{HUE}"><div style="position:absolute;left:{ox}px;top:{oy}px">{logo}</div>{ann}{txt}{tag("La idea")}{tag("02", x=1510)}</div>'
    shot(page(bb), "board/02_idea.png", Wb, Hb)

# 3 · versiones
if want("versiones"):
    cell = lambda inner, bg, cap, capc=NIE, w=460, h=330: (f'<div style="display:flex;flex-direction:column;gap:10px"><div style="width:{w}px;height:{h}px;background:{bg};display:flex;align-items:center;justify-content:center">{inner}</div>'
                                                           f'<div class=lab style="color:{NIE}">{cap}</div></div>')
    sizes = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">{inl([(SMALL if s<=24 else SYM, PET)], w=s)}<span style="font-size:11px;color:{NIE}">{s} px</span></div>' for s in (16, 24, 44))
    sizes += f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px"><img src="{M}/iconos/favicon.svg" style="width:32px"><span style="font-size:11px;color:{NIE}">favicon</span></div>'
    sizes += f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">{inl(layers(WH,"color"), w=150)}<span style="font-size:11px;color:{NIE}">una línea, 150 px</span></div>'
    b = f'''<div class=b style="background:#EAE5DB;padding:96px 64px 0 64px;display:grid;grid-template-columns:460px 460px 460px;gap:26px 32px">
      {cell(inl(layers(WV,"color"), w=340), HUE, "Principal")}
      {cell(inl(layers(WH,"color"), w=390), HUE, "Una línea · web y documentos")}
      {cell(inl(layers(WV,"negativo"), w=340), PET, "Negativo · filete y ojos en oro")}
      {cell(inl(layers(None,"oro"), w=150), PETD, "Los ojos · avatar y sello", w=460, h=250)}
      {cell(inl(layers(WV,"tinta"), w=320), "#FFFFFF", "Una tinta", w=460, h=250)}
      {cell('<div style="display:flex;gap:26px;align-items:flex-end">' + sizes + '</div>', HUE, "Tamaños reales y reducido", w=460, h=250)}
      {tag("Versiones")}{tag("03", x=1510)}</div>'''
    shot(page(b), "board/03_versiones.png", Wb, Hb)

# 4 · color y letra
if want("color"):
    sw = lambda c, n, hx, rgb, use, tc=HUE, br="": (f'<div style="flex:1;height:420px;background:{c};{br}padding:28px;display:flex;flex-direction:column;justify-content:flex-end;gap:6px;color:{tc}">'
        f'<div class=serif style="font-size:34px;font-weight:500">{n}</div><div style="font-size:15px;letter-spacing:1px">{hx} · {rgb}</div><div style="font-size:15px;opacity:.85">{use}</div></div>')
    b = f'''<div class=b style="background:{HUE};padding:110px 64px 0 64px;display:flex;flex-direction:column;gap:46px">
      <div style="display:flex;gap:0">{sw(PET,"Petróleo","#134150","RGB 19 65 80","Autoridad. 9,7:1 con hueso.")}{sw(ORO,"Oro viejo","#C2A36B","RGB 194 163 107","Un solo toque. 4,6:1 sobre petróleo.",TIN)}{sw(HUE,"Hueso","#F4F0E8","RGB 244 240 232","El papel.",TIN,f"border:1px solid #D8D1C4;")}{sw(TIN,"Tinta","#14252B","RGB 20 37 43","Texto. 14:1 sobre hueso.")}</div>
      <div style="display:flex;gap:80px;align-items:flex-end">
        <div style="flex:1.2"><div class=lab style="color:{NIE}">Bodoni Moda · nombre y titulares</div><div class=serif style="font-size:64px;font-weight:500;color:{PET};line-height:1.1;margin-top:10px">Cada cuenta, explicada.</div></div>
        <div style="flex:1"><div class=lab style="color:{NIE}">Jost · texto, datos y etiquetas</div><div style="font-size:20px;line-height:1.55;margin-top:12px">Contabilidad continua para empresas y negocios, con un responsable que conoce su caso. <span style="font-feature-settings:'tnum'">Bs 12.480,00</span></div></div></div>
      {tag("Color y letra")}{tag("04", x=1510)}</div>'''
    shot(page(b), "board/04_color.png", Wb, Hb)

# 5 · aplicaciones: tarjeta y placa
if want("apps1"):
    foil = f"linear-gradient(135deg,#D8BE86 0%,#B8955A 45%,#E3CD98 60%,#A9864B 100%)"
    card_front = f'<div style="width:504px;height:280px;background:{PET};box-shadow:0 22px 40px rgba(10,30,38,.35);display:flex;align-items:center;justify-content:center">{inl(layers(WV,"negativo"), w=260)}</div>'
    card_back = f'''<div style="width:504px;height:280px;background:{HUE};box-shadow:0 22px 40px rgba(10,30,38,.25);padding:38px 40px;display:flex;flex-direction:column;justify-content:space-between">
      <div><div class=serif style="font-size:24px;font-weight:500;letter-spacing:3px;color:{PET}">[NOMBRE DEL PROFESIONAL]</div><div style="font-size:14px;letter-spacing:2px;text-transform:uppercase;color:{NIE};margin-top:8px">[Cargo confirmado]</div></div>
      <div style="display:flex;justify-content:space-between;align-items:flex-end"><div style="font-size:14px;line-height:1.7;color:{TIN}">[Teléfono]<br>[Correo corporativo]<br>La Paz, Bolivia</div>{inl(layers(None,"color"), w=52)}</div></div>'''
    plate = f'''<div style="width:520px;height:640px;background:#23434E;display:flex;align-items:center;justify-content:center;box-shadow:inset 0 0 120px rgba(0,0,0,.35)">
      <div style="width:360px;height:240px;background:{foil};box-shadow:0 14px 28px rgba(0,0,0,.45);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px;position:relative">
        {inl(layers(WV,"tinta"), w=250)}
        <div style="font-size:10px;letter-spacing:3px;color:#3A3020">CONTABILIDAD Y ASESORÍA · PISO [__]</div>
        {''.join(f'<div style="position:absolute;{p};width:9px;height:9px;border-radius:5px;background:#8E7040"></div>' for p in ("left:14px;top:14px","right:14px;top:14px","left:14px;bottom:14px","right:14px;bottom:14px"))}</div></div>'''
    b = f'''<div class=b style="background:#E4DED2">
      <div style="position:absolute;left:80px;top:130px;display:flex;flex-direction:column;gap:40px">{card_front}{card_back}</div>
      <div style="position:absolute;left:1000px;top:130px">{plate}</div>
      <div class=lab style="position:absolute;left:80px;top:846px;color:{NIE}">Tarjeta 90 × 50 mm · filete y ojos en oro en caliente</div>
      <div class=lab style="position:absolute;left:1000px;top:800px;width:520px;color:{NIE}">Placa de bronce grabada, entrada de la oficina</div>
      {tag("Aplicaciones")}{tag("05", x=1510)}</div>'''
    shot(page(b), "board/05_tarjeta_placa.png", Wb, Hb)

# 6 · aplicaciones: papelería y web
if want("apps2"):
    lines = "".join(f'<div style="height:5px;width:{w}%;background:#E3DED3;margin-top:11px"></div>' for w in (92, 88, 95, 60, 0, 90, 94, 72))
    letter = f'''<div style="width:400px;height:566px;background:#FBF9F5;box-shadow:0 18px 36px rgba(10,30,38,.22);padding:44px 46px;display:flex;flex-direction:column">
      <div style="display:flex;justify-content:center">{inl(layers(WV,"color"), w=180)}</div>
      <div style="height:1px;background:{ORO};margin:26px 0 22px"></div>
      <div style="font-size:11px;letter-spacing:2px;color:{NIE}">LA PAZ, [FECHA]</div>
      <div class=serif style="font-size:20px;font-weight:500;color:{PET};margin-top:16px">Resumen de cierre · [período]</div>{lines}
      <div style="flex:1"></div><div style="font-size:10px;letter-spacing:1.5px;color:{NIE};text-align:center">GABINETE CONTABLE · [DIRECCIÓN] · [TELÉFONO]</div></div>'''
    envelope = f'''<div style="width:420px;height:230px;background:{PET};box-shadow:0 18px 36px rgba(10,30,38,.3);position:relative;display:flex;align-items:center;justify-content:center">
      <div style="position:absolute;left:0;top:0;width:0;height:0;border-left:210px solid transparent;border-right:210px solid transparent;border-top:120px solid #174A5B"></div>
      <div style="position:relative;width:74px;height:74px;border-radius:37px;background:{ORO};display:flex;align-items:center;justify-content:center;margin-top:-10px">{inl(layers(None,"tinta"), w=50)}</div></div>'''
    web = f'''<div style="width:640px;height:400px;background:{HUE};box-shadow:0 18px 36px rgba(10,30,38,.22);overflow:hidden">
      <div style="height:34px;background:#DDD6CA;display:flex;align-items:flex-end;padding-left:10px"><div style="background:{HUE};height:26px;padding:0 12px;display:flex;align-items:center;gap:8px;font-size:12px"><img src="{M}/iconos/favicon.svg" style="width:14px">Gabinete Contable</div></div>
      <div style="padding:20px 30px;display:flex;justify-content:space-between;align-items:center">{inl(layers(WH,"color"), w=230)}
        <div style="display:flex;gap:16px;font-size:10px;letter-spacing:1.6px;color:{TIN}"><span>CONTABILIDAD</span><span>SERVICIOS</span><span>EL GABINETE</span></div></div>
      <div style="padding:38px 30px 0"><div class=serif style="font-size:44px;font-weight:500;line-height:1.08;color:{PET}">Sus libros en orden.<br>Cada cuenta, explicada.</div>
        <div style="font-size:14px;color:{NIE};margin-top:14px;line-height:1.5;width:380px">Contabilidad continua para empresas, con un responsable que conoce su caso.</div>
        <div style="display:inline-block;margin-top:20px;background:{PET};color:{HUE};font-size:12px;letter-spacing:2px;padding:12px 18px">CONVERSEMOS</div></div></div>'''
    avatar = f'<img src="{M}/iconos/gc_avatar_1080.png" style="width:150px;height:150px;border-radius:75px;box-shadow:0 10px 24px rgba(10,30,38,.25)">'
    b = f'''<div class=b style="background:#E4DED2">
      <div style="position:absolute;left:80px;top:130px">{letter}</div>
      <div style="position:absolute;left:520px;top:466px">{envelope}</div>
      <div style="position:absolute;left:880px;top:130px">{web}</div>
      <div style="position:absolute;left:1000px;top:590px;display:flex;align-items:center;gap:26px">{avatar}<div><div class=serif style="font-size:24px;font-weight:500;color:{TIN}">Gabinete Contable</div><div style="font-size:14px;color:{NIE};margin-top:4px">Perfil de empresa · La Paz</div></div></div>
      <div class=lab style="position:absolute;left:80px;top:720px;width:420px;color:{NIE}">Carta A4, sobre con sello de oro</div>
      <div class=lab style="position:absolute;left:880px;top:780px;width:640px;color:{NIE}">Web, favicon y avatar de perfil</div>
      {tag("Aplicaciones")}{tag("06", x=1510)}</div>'''
    shot(page(b), "board/06_papeleria_web.png", Wb, Hb)
