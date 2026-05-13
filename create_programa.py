import json

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

head_end = html.find('</head>')
head = html[:head_end + 7]

nav_start = html.find('<nav class="nav"')
nav_end = html.find('<!-- HERO -->')
nav = html[nav_start:nav_end]

# Update nav links to point to index.html sections
nav = nav.replace('href="#inicio"', 'href="index.html#inicio"')
nav = nav.replace('href="#sobre"', 'href="index.html#sobre"')
nav = nav.replace('href="#servicos"', 'href="index.html#servicos"')
nav = nav.replace('href="#depoimentos"', 'href="index.html#depoimentos"')
nav = nav.replace('href="#contato"', 'href="index.html#contato"')

footer_start = html.find('<footer>')
footer_end = html.find('</footer>') + 9
footer = html[footer_start:footer_end]

# Update footer links
footer = footer.replace('href="#servicos"', 'href="index.html#servicos"')
footer = footer.replace('href="#contato"', 'href="index.html#contato"')
footer = footer.replace('href="#sobre"', 'href="index.html#sobre"')
footer = footer.replace('href="#depoimentos"', 'href="index.html#depoimentos"')

scripts_start = html.find('<script>')
scripts = html[scripts_start:]

# We will inject the new LANG object inside scripts. 
# But let's build the main body first.

content_html = """
    <!-- HERO PROGRAMA -->
    <section class="hero" id="inicio" style="min-height: 50vh; padding-top: 120px; align-items: start;">
      <div class="hero-bg"></div>
      <div class="hero-lines"></div>
      <div class="container" style="position: relative; z-index: 1;">
        <div class="hero-eyebrow reveal prog-eyebrow">
          Programa de Assessoria
        </div>
        <h1 class="reveal prog-h1" data-delay="1" style="font-size: clamp(2rem, 3.5vw, 3rem);">
          Programa de Assessoria de <br /><em>Gestão Integrada</em>
        </h1>
        <p class="hero-sub reveal prog-sub" data-delay="2" style="max-width: 600px;">
          Desenvolvimento contínuo para empresas que querem evoluir de forma estruturada.
        </p>
      </div>
    </section>

    <!-- APRESENTAÇÃO -->
    <section class="sobre" style="padding-top: 60px;">
      <div class="container" style="grid-template-columns: 1fr;">
        <div class="reveal-left">
          <div class="sobre-label prog-apres-label">Apresentação do Programa</div>
          <h2 class="prog-apres-h2">Desenvolvimento Contínuo</h2>
          <div class="pilares-grid" style="grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); margin-top: 30px;">
            <div class="pilar-card">
              <div class="pilar-icon">🔄</div>
              <h3 class="prog-apres-p1-h">Acompanhamento</h3>
              <p class="prog-apres-p1">Programa de acompanhamento contínuo no formato trimestral, semestral ou anual.</p>
            </div>
            <div class="pilar-card">
              <div class="pilar-icon">🔗</div>
              <h3 class="prog-apres-p2-h">Integração</h3>
              <p class="prog-apres-p2">Integração entre finanças, comercial, produção e gestão de pessoas.</p>
            </div>
            <div class="pilar-card">
              <div class="pilar-icon">👥</div>
              <h3 class="prog-apres-p3-h">Equipe</h3>
              <p class="prog-apres-p3">Desenvolvimento contínuo da equipe de gestores.</p>
            </div>
            <div class="pilar-card">
              <div class="pilar-icon">💻</div>
              <h3 class="prog-apres-p4-h">Modelo Híbrido</h3>
              <p class="prog-apres-p4">Treinamentos + reuniões privadas + suporte consultivo.</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- COMO FUNCIONA -->
    <section class="pilares">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-label prog-func-label">Como o Programa Funciona</div>
          <h2 class="prog-func-h2">Dinâmica dos <em>Encontros</em></h2>
        </div>
        <div class="pq-list reveal-right" style="max-width: 800px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
          <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-func-i1">Treinamentos cíclicos de curta duração</p></div>
          <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-func-i2">Reuniões online privadas mensais</p></div>
          <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-func-i3">Discussão de problemas reais da empresa</p></div>
          <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-func-i4">Análise de relatórios apresentados pelos clientes nas reuniões privadas</p></div>
          <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-func-i5">Materiais de apoio em todos os encontros</p></div>
          <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-func-i6">Participação de diferentes consultores especialistas</p></div>
        </div>
      </div>
    </section>

    <!-- TEMAS ABORDADOS -->
    <section class="servicos">
      <div class="container">
        <div class="section-head reveal">
          <div class="section-label prog-temas-label">Temas Abordados</div>
          <h2 class="prog-temas-h2">Áreas de <em>Desenvolvimento</em></h2>
        </div>
        <div class="servicos-grid" style="grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));">
          <div class="servico-card">
            <h3 class="prog-temas-t1">Gestão Financeira</h3>
            <ul style="color: rgba(255,255,255,0.45); font-size: 0.875rem; line-height: 1.75; list-style-type: disc; padding-left: 20px;">
              <li class="prog-temas-t1-i1">Custos</li>
              <li class="prog-temas-t1-i2">Precificação</li>
              <li class="prog-temas-t1-i3">Fluxo de Caixa</li>
              <li class="prog-temas-t1-i4">Orçamento</li>
              <li class="prog-temas-t1-i5">Indicadores</li>
            </ul>
          </div>
          <div class="servico-card">
            <h3 class="prog-temas-t2">Área Comercial</h3>
            <ul style="color: rgba(255,255,255,0.45); font-size: 0.875rem; line-height: 1.75; list-style-type: disc; padding-left: 20px;">
              <li class="prog-temas-t2-i1">Estratégia comercial</li>
              <li class="prog-temas-t2-i2">Margens</li>
              <li class="prog-temas-t2-i3">Relacionamento com clientes</li>
              <li class="prog-temas-t2-i4">Performance de vendas</li>
            </ul>
          </div>
          <div class="servico-card">
            <h3 class="prog-temas-t3">Produção e Operações</h3>
            <ul style="color: rgba(255,255,255,0.45); font-size: 0.875rem; line-height: 1.75; list-style-type: disc; padding-left: 20px;">
              <li class="prog-temas-t3-i1">Lean Manufacturing</li>
              <li class="prog-temas-t3-i2">Produtividade</li>
              <li class="prog-temas-t3-i3">Processos</li>
              <li class="prog-temas-t3-i4">Redução de desperdícios</li>
            </ul>
          </div>
          <div class="servico-card">
            <h3 class="prog-temas-t4">Gestão de Pessoas</h3>
            <ul style="color: rgba(255,255,255,0.45); font-size: 0.875rem; line-height: 1.75; list-style-type: disc; padding-left: 20px;">
              <li class="prog-temas-t4-i1">Liderança</li>
              <li class="prog-temas-t4-i2">Integração</li>
              <li class="prog-temas-t4-i3">Comunicação</li>
              <li class="prog-temas-t4-i4">Desenvolvimento de equipes</li>
            </ul>
          </div>
        </div>
      </div>
    </section>

    <!-- DIFERENCIAL -->
    <section class="sobre" style="background: var(--paper);">
      <div class="container" style="grid-template-columns: 1fr;">
        <div class="reveal-left" style="text-align: center;">
          <div class="sobre-label prog-dif-label">Diferencial do Programa</div>
          <h2 class="prog-dif-h2">O que nos torna <em>únicos</em></h2>
          <div class="pq-list" style="max-width: 800px; margin: 40px auto 0; text-align: left; display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px;">
            <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-dif-i1">Treinamentos recorrentes em temas clássicos e atuais</p></div>
            <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-dif-i2">Ambiente de troca entre empresas e profissionais</p></div>
            <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-dif-i3">Desenvolvimento contínuo da equipe de gestores</p></div>
            <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-dif-i4">Integração entre áreas da empresa como ponto focal</p></div>
            <div class="pq-item"><div class="pq-check"><svg viewBox="0 0 12 12"><polyline points="2,6 5,9 10,3" /></svg></div><p class="prog-dif-i5">Possibilidade de aprofundamento através de projetos específicos</p></div>
          </div>
        </div>
      </div>
    </section>

    <!-- REUNIÕES PRIVADAS & BENEFÍCIOS -->
    <section class="sobre" style="background: var(--white);">
      <div class="container" style="grid-template-columns: 1fr 1fr; gap: 60px; align-items: start;">
        <div class="reveal-left">
          <div class="sobre-label prog-reun-label">Reuniões Privadas</div>
          <h2 class="prog-reun-h2">Acompanhamento <em>Personalizado</em></h2>
          
          <h3 class="prog-reun-sub1" style="font-family: var(--ff-head); margin: 30px 0 15px; font-size: 1.2rem;">O Programa Contempla:</h3>
          <ul style="list-style: none;">
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--gold);">✓</span> <span class="prog-reun-1-1">Cada empresa pode agendar reuniões online privadas</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--gold);">✓</span> <span class="prog-reun-1-2">Discussão confidencial sobre desafios reais do dia a dia</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--gold);">✓</span> <span class="prog-reun-1-3">Orientação personalizada</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--gold);">✓</span> <span class="prog-reun-1-4">Participação direta dos consultores</span></li>
          </ul>

          <h3 class="prog-reun-sub2" style="font-family: var(--ff-head); margin: 30px 0 15px; font-size: 1.2rem;">O Programa Possibilita (Contratação Extra):</h3>
          <ul style="list-style: none;">
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--ink3);">+</span> <span class="prog-reun-2-1">Possibilidade de reuniões extras</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--ink3);">+</span> <span class="prog-reun-2-2">Encontros presenciais com os consultores</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--ink3);">+</span> <span class="prog-reun-2-3">Projetos específicos de consultoria</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--ink3);">+</span> <span class="prog-reun-2-4">Contratação de especialistas parceiros</span></li>
            <li style="margin-bottom: 10px; display: flex; gap: 10px;"><span style="color: var(--ink3);">+</span> <span class="prog-reun-2-5">Formação de equipes dedicadas para projetos estratégicos</span></li>
          </ul>
        </div>
        
        <div class="reveal-right">
          <div class="sobre-label prog-ben-label">Benefícios</div>
          <h2 class="prog-ben-h2">Resultados para o <em>Cliente</em></h2>
          <div class="pilares-grid" style="grid-template-columns: 1fr; gap: 10px; background: transparent;">
            <div class="pilar-card" style="padding: 20px; border: 1px solid var(--rule2); display: flex; align-items: center; gap: 15px;">
              <div style="font-size: 1.5rem;">🎓</div> <span class="prog-ben-1" style="font-weight: 500;">Capacitação contínua dos gestores</span>
            </div>
            <div class="pilar-card" style="padding: 20px; border: 1px solid var(--rule2); display: flex; align-items: center; gap: 15px;">
              <div style="font-size: 1.5rem;">🤝</div> <span class="prog-ben-2" style="font-weight: 500;">Equipes mais integradas</span>
            </div>
            <div class="pilar-card" style="padding: 20px; border: 1px solid var(--rule2); display: flex; align-items: center; gap: 15px;">
              <div style="font-size: 1.5rem;">⭐</div> <span class="prog-ben-3" style="font-weight: 500;">Contato constante com especialistas</span>
            </div>
            <div class="pilar-card" style="padding: 20px; border: 1px solid var(--rule2); display: flex; align-items: center; gap: 15px;">
              <div style="font-size: 1.5rem;">📈</div> <span class="prog-ben-4" style="font-weight: 500;">Atualização permanente e melhoria da tomada de decisão</span>
            </div>
            <div class="pilar-card" style="padding: 20px; border: 1px solid var(--rule2); display: flex; align-items: center; gap: 15px;">
              <div style="font-size: 1.5rem;">🗣️</div> <span class="prog-ben-5" style="font-weight: 500;">Redução do isolamento das lideranças e troca de experiências</span>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- PLANOS E CONDIÇÕES -->
    <section class="contato" style="background: var(--paper); padding-top: 80px; padding-bottom: 80px;">
      <div class="container" style="text-align: center;">
        <div class="sobre-label prog-plan-label">Planos e Condições</div>
        <h2 class="prog-plan-h2">Escolha o plano ideal para sua empresa</h2>
        
        <div class="pilares-grid" style="grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); margin-top: 50px; gap: 20px; background: transparent;">
          <div class="pilar-card" style="border: 1px solid var(--rule); border-top: 4px solid var(--ink3); border-radius: 4px;">
            <h3 class="prog-plan-1-h" style="font-size: 1.5rem; margin-bottom: 20px;">Plano Trimestral</h3>
            <p class="prog-plan-1-p">Para empresas que buscam um ciclo focado de aprimoramento rápido e direto.</p>
            <a href="index.html#contato" class="btn-outline prog-plan-btn" style="margin-top: 30px; width: 100%; justify-content: center;">Consultar Valores</a>
          </div>
          <div class="pilar-card" style="border: 1px solid var(--gold); border-top: 4px solid var(--gold); border-radius: 4px; position: relative;">
            <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--gold); color: white; padding: 4px 12px; font-size: 0.7rem; font-weight: bold; border-radius: 20px; letter-spacing: 1px;" class="prog-plan-rec">MAIS ESCOLHIDO</div>
            <h3 class="prog-plan-2-h" style="font-size: 1.5rem; margin-bottom: 20px;">Plano Semestral</h3>
            <p class="prog-plan-2-p">Desenvolvimento consistente e integração avançada das áreas da empresa.</p>
            <a href="index.html#contato" class="btn-primary prog-plan-btn" style="margin-top: 30px; width: 100%; justify-content: center;">Consultar Valores</a>
          </div>
          <div class="pilar-card" style="border: 1px solid var(--rule); border-top: 4px solid var(--ink); border-radius: 4px;">
            <h3 class="prog-plan-3-h" style="font-size: 1.5rem; margin-bottom: 20px;">Plano Anual</h3>
            <p class="prog-plan-3-p">Transformação profunda da cultura organizacional e gestão estratégica contínua.</p>
            <a href="index.html#contato" class="btn-outline prog-plan-btn" style="margin-top: 30px; width: 100%; justify-content: center;">Consultar Valores</a>
          </div>
        </div>
      </div>
    </section>
    
    <!-- CONTRATO E ADESÃO -->
    <section class="sobre" style="background: var(--white); padding-top: 60px; padding-bottom: 60px;">
      <div class="container" style="text-align: center;">
        <div class="sobre-label prog-cont-label">Contrato e Adesão</div>
        <h2 class="prog-cont-h2">Formalize sua participação</h2>
        <div style="margin-top: 40px; display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;">
          <a href="#" class="btn-primary prog-cont-btn1">Visualizar Contrato</a>
          <a href="#" class="btn-outline prog-cont-btn2">Download do PDF</a>
        </div>
        <p style="margin-top: 30px; font-size: 0.85rem; color: var(--ink3); font-style: italic;" class="prog-cont-p">
          * Área futura para pagamento online em desenvolvimento.
        </p>
      </div>
    </section>

    <!-- CHAMADA FINAL -->
    <section class="servicos" style="background: var(--gold); padding: 80px 0; text-align: center;">
      <div class="container">
        <h2 class="prog-cta-h2" style="font-family: var(--ff-head); color: var(--white); font-size: clamp(2rem, 3vw, 2.8rem); margin-bottom: 20px;">
          Desenvolva sua equipe de forma contínua e integrada.
        </h2>
        <a href="index.html#contato" class="btn-primary prog-cta-btn" style="background: var(--ink); color: var(--white); border: none; font-size: 1rem; padding: 16px 36px; text-transform: none; font-weight: 600;">
          Agende uma reunião online
        </a>
      </div>
    </section>
"""

# Modify scripts to inject translations for BOTH index and programa
# Since index.html has a specific LANG object, we will inject new keys directly into it in our new file.

scripts = scripts.replace("const LANG = {", """const LANG = {
        pt: {
          '.prog-eyebrow': 'Programa de Assessoria',
          '.prog-h1': 'Programa de Assessoria de <br /><em>Gestão Integrada</em>',
          '.prog-sub': 'Desenvolvimento contínuo para empresas que querem evoluir de forma estruturada.',
          '.prog-apres-label': 'Apresentação do Programa',
          '.prog-apres-h2': 'Desenvolvimento Contínuo',
          '.prog-apres-p1-h': 'Acompanhamento',
          '.prog-apres-p1': 'Programa de acompanhamento contínuo no formato trimestral, semestral ou anual.',
          '.prog-apres-p2-h': 'Integração',
          '.prog-apres-p2': 'Integração entre finanças, comercial, produção e gestão de pessoas.',
          '.prog-apres-p3-h': 'Equipe',
          '.prog-apres-p3': 'Desenvolvimento contínuo da equipe de gestores.',
          '.prog-apres-p4-h': 'Modelo Híbrido',
          '.prog-apres-p4': 'Treinamentos + reuniões privadas + suporte consultivo.',
          '.prog-func-label': 'Como o Programa Funciona',
          '.prog-func-h2': 'Dinâmica dos <em>Encontros</em>',
          '.prog-func-i1': 'Treinamentos cíclicos de curta duração',
          '.prog-func-i2': 'Reuniões online privadas mensais',
          '.prog-func-i3': 'Discussão de problemas reais da empresa',
          '.prog-func-i4': 'Análise de relatórios apresentados pelos clientes nas reuniões privadas',
          '.prog-func-i5': 'Materiais de apoio em todos os encontros',
          '.prog-func-i6': 'Participação de diferentes consultores especialistas',
          '.prog-temas-label': 'Temas Abordados',
          '.prog-temas-h2': 'Áreas de <em>Desenvolvimento</em>',
          '.prog-temas-t1': 'Gestão Financeira',
          '.prog-temas-t1-i1': 'Custos',
          '.prog-temas-t1-i2': 'Precificação',
          '.prog-temas-t1-i3': 'Fluxo de Caixa',
          '.prog-temas-t1-i4': 'Orçamento',
          '.prog-temas-t1-i5': 'Indicadores',
          '.prog-temas-t2': 'Área Comercial',
          '.prog-temas-t2-i1': 'Estratégia comercial',
          '.prog-temas-t2-i2': 'Margens',
          '.prog-temas-t2-i3': 'Relacionamento com clientes',
          '.prog-temas-t2-i4': 'Performance de vendas',
          '.prog-temas-t3': 'Produção e Operações',
          '.prog-temas-t3-i1': 'Lean Manufacturing',
          '.prog-temas-t3-i2': 'Produtividade',
          '.prog-temas-t3-i3': 'Processos',
          '.prog-temas-t3-i4': 'Redução de desperdícios',
          '.prog-temas-t4': 'Gestão de Pessoas',
          '.prog-temas-t4-i1': 'Liderança',
          '.prog-temas-t4-i2': 'Integração',
          '.prog-temas-t4-i3': 'Comunicação',
          '.prog-temas-t4-i4': 'Desenvolvimento de equipes',
          '.prog-dif-label': 'Diferencial do Programa',
          '.prog-dif-h2': 'O que nos torna <em>únicos</em>',
          '.prog-dif-i1': 'Treinamentos recorrentes em temas clássicos e atuais',
          '.prog-dif-i2': 'Ambiente de troca entre empresas e profissionais',
          '.prog-dif-i3': 'Desenvolvimento contínuo da equipe de gestores',
          '.prog-dif-i4': 'Integração entre áreas da empresa como ponto focal',
          '.prog-dif-i5': 'Possibilidade de aprofundamento através de projetos específicos',
          '.prog-reun-label': 'Reuniões Privadas',
          '.prog-reun-h2': 'Acompanhamento <em>Personalizado</em>',
          '.prog-reun-sub1': 'O Programa Contempla:',
          '.prog-reun-1-1': 'Cada empresa pode agendar reuniões online privadas',
          '.prog-reun-1-2': 'Discussão confidencial sobre desafios reais do dia a dia',
          '.prog-reun-1-3': 'Orientação personalizada',
          '.prog-reun-1-4': 'Participação direta dos consultores',
          '.prog-reun-sub2': 'O Programa Possibilita (Contratação Extra):',
          '.prog-reun-2-1': 'Possibilidade de reuniões extras',
          '.prog-reun-2-2': 'Encontros presenciais com os consultores',
          '.prog-reun-2-3': 'Projetos específicos de consultoria',
          '.prog-reun-2-4': 'Contratação de especialistas parceiros',
          '.prog-reun-2-5': 'Formação de equipes dedicadas para projetos estratégicos',
          '.prog-ben-label': 'Benefícios',
          '.prog-ben-h2': 'Resultados para o <em>Cliente</em>',
          '.prog-ben-1': 'Capacitação contínua dos gestores',
          '.prog-ben-2': 'Equipes mais integradas',
          '.prog-ben-3': 'Contato constante com especialistas',
          '.prog-ben-4': 'Atualização permanente e melhoria da tomada de decisão',
          '.prog-ben-5': 'Redução do isolamento das lideranças e troca de experiências',
          '.prog-plan-label': 'Planos e Condições',
          '.prog-plan-h2': 'Escolha o plano ideal para sua empresa',
          '.prog-plan-1-h': 'Plano Trimestral',
          '.prog-plan-1-p': 'Para empresas que buscam um ciclo focado de aprimoramento rápido e direto.',
          '.prog-plan-2-h': 'Plano Semestral',
          '.prog-plan-2-p': 'Desenvolvimento consistente e integração avançada das áreas da empresa.',
          '.prog-plan-3-h': 'Plano Anual',
          '.prog-plan-3-p': 'Transformação profunda da cultura organizacional e gestão estratégica contínua.',
          '.prog-plan-btn': 'Consultar Valores',
          '.prog-plan-rec': 'MAIS ESCOLHIDO',
          '.prog-cont-label': 'Contrato e Adesão',
          '.prog-cont-h2': 'Formalize sua participação',
          '.prog-cont-btn1': 'Visualizar Contrato',
          '.prog-cont-btn2': 'Download do PDF',
          '.prog-cont-p': '* Área futura para pagamento online em desenvolvimento.',
          '.prog-cta-h2': 'Desenvolva sua equipe de forma contínua e integrada.',
          '.prog-cta-btn': 'Agende uma reunião online',
""")

scripts = scripts.replace("en: {", """en: {
          '.prog-eyebrow': 'Management Advisory Program',
          '.prog-h1': 'Integrated Management <br /><em>Advisory Program</em>',
          '.prog-sub': 'Continuous development for companies seeking structured growth.',
          '.prog-apres-label': 'Program Presentation',
          '.prog-apres-h2': 'Continuous Development',
          '.prog-apres-p1-h': 'Monitoring',
          '.prog-apres-p1': 'Continuous monitoring program in quarterly, semi-annual, or annual format.',
          '.prog-apres-p2-h': 'Integration',
          '.prog-apres-p2': 'Integration between finance, commercial, production, and people management.',
          '.prog-apres-p3-h': 'Team',
          '.prog-apres-p3': 'Continuous development of the management team.',
          '.prog-apres-p4-h': 'Hybrid Model',
          '.prog-apres-p4': 'Training + private meetings + consultative support.',
          '.prog-func-label': 'How the Program Works',
          '.prog-func-h2': 'Meeting <em>Dynamics</em>',
          '.prog-func-i1': 'Short-duration cyclical training',
          '.prog-func-i2': 'Monthly private online meetings',
          '.prog-func-i3': 'Discussion of real company problems',
          '.prog-func-i4': 'Analysis of reports presented by clients in private meetings',
          '.prog-func-i5': 'Support materials in all meetings',
          '.prog-func-i6': 'Participation of different specialist consultants',
          '.prog-temas-label': 'Covered Themes',
          '.prog-temas-h2': 'Areas of <em>Development</em>',
          '.prog-temas-t1': 'Financial Management',
          '.prog-temas-t1-i1': 'Costs',
          '.prog-temas-t1-i2': 'Pricing',
          '.prog-temas-t1-i3': 'Cash Flow',
          '.prog-temas-t1-i4': 'Budget',
          '.prog-temas-t1-i5': 'Indicators',
          '.prog-temas-t2': 'Commercial Area',
          '.prog-temas-t2-i1': 'Commercial strategy',
          '.prog-temas-t2-i2': 'Margins',
          '.prog-temas-t2-i3': 'Customer relationship',
          '.prog-temas-t2-i4': 'Sales performance',
          '.prog-temas-t3': 'Production and Operations',
          '.prog-temas-t3-i1': 'Lean Manufacturing',
          '.prog-temas-t3-i2': 'Productivity',
          '.prog-temas-t3-i3': 'Processes',
          '.prog-temas-t3-i4': 'Waste reduction',
          '.prog-temas-t4': 'People Management',
          '.prog-temas-t4-i1': 'Leadership',
          '.prog-temas-t4-i2': 'Integration',
          '.prog-temas-t4-i3': 'Communication',
          '.prog-temas-t4-i4': 'Team development',
          '.prog-dif-label': 'Program Differentiator',
          '.prog-dif-h2': 'What makes us <em>unique</em>',
          '.prog-dif-i1': 'Recurring training on classic and current themes',
          '.prog-dif-i2': 'Exchange environment between companies and professionals',
          '.prog-dif-i3': 'Continuous development of the management team',
          '.prog-dif-i4': 'Integration between company areas as a focal point',
          '.prog-dif-i5': 'Possibility of deepening through specific projects',
          '.prog-reun-label': 'Private Meetings',
          '.prog-reun-h2': 'Personalized <em>Guidance</em>',
          '.prog-reun-sub1': 'The Program Includes:',
          '.prog-reun-1-1': 'Each company can schedule private online meetings',
          '.prog-reun-1-2': 'Confidential discussion about real day-to-day challenges',
          '.prog-reun-1-3': 'Personalized guidance',
          '.prog-reun-1-4': 'Direct participation of consultants',
          '.prog-reun-sub2': 'The Program Enables (Extra Contracting):',
          '.prog-reun-2-1': 'Possibility of extra meetings',
          '.prog-reun-2-2': 'Face-to-face meetings with consultants',
          '.prog-reun-2-3': 'Specific consulting projects',
          '.prog-reun-2-4': 'Hiring of partner specialists',
          '.prog-reun-2-5': 'Formation of dedicated teams for strategic projects',
          '.prog-ben-label': 'Benefits',
          '.prog-ben-h2': 'Results for the <em>Client</em>',
          '.prog-ben-1': 'Continuous training of managers',
          '.prog-ben-2': 'More integrated teams',
          '.prog-ben-3': 'Constant contact with specialists',
          '.prog-ben-4': 'Permanent update and improved decision-making',
          '.prog-ben-5': 'Reduction of leadership isolation and exchange of experiences',
          '.prog-plan-label': 'Plans and Conditions',
          '.prog-plan-h2': 'Choose the ideal plan for your company',
          '.prog-plan-1-h': 'Quarterly Plan',
          '.prog-plan-1-p': 'For companies seeking a focused cycle of fast and direct improvement.',
          '.prog-plan-2-h': 'Semi-annual Plan',
          '.prog-plan-2-p': 'Consistent development and advanced integration of company areas.',
          '.prog-plan-3-h': 'Annual Plan',
          '.prog-plan-3-p': 'Profound transformation of organizational culture and continuous strategic management.',
          '.prog-plan-btn': 'Consult Pricing',
          '.prog-plan-rec': 'MOST CHOSEN',
          '.prog-cont-label': 'Contract and Accession',
          '.prog-cont-h2': 'Formalize your participation',
          '.prog-cont-btn1': 'View Contract',
          '.prog-cont-btn2': 'Download PDF',
          '.prog-cont-p': '* Future area for online payment under development.',
          '.prog-cta-h2': 'Develop your team continuously and integrally.',
          '.prog-cta-btn': 'Schedule an online meeting',
""")


new_html = head + '\n<body>\n' + nav + '\n' + content_html + '\n' + footer + '\n' + scripts

with open('programa.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

# We don't need to update index.html again, but just in case:
index_html = html.replace('<a href="#contato" class="servico-link">Saiba mais →</a>', '<a href="programa.html" class="servico-link">Saiba mais →</a>', 1)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)
