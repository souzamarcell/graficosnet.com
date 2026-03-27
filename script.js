let dados = [
  {
    id: 1,
    titulo: 'Casa de Ferragens Nova Europa',
    cat: 'Comércio',
    preco: 'Consulte no local',
    desc: 'Loja completa de ferramentas e materiais para construção. Atendimento especializado e variedade de produtos para profissionais e domésticos.',
    tags: ['ferramentas', 'construção', 'loja'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 99999-1234',
    badge: 'Destaque',
  },
  {
    id: 2,
    titulo: 'Marmoraria Nova Europa',
    cat: 'Serviços',
    preco: 'Sob consulta',
    desc: 'Especializada em mármore e granito para cozinhas, banheiros e áreas externas. Orçamento rápido e atendimento na região.',
    tags: ['mármore', 'granito', 'reforma'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 98888-4321',
    badge: '',
  },
  {
    id: 3,
    titulo: 'Agro Jardim & Irrigação',
    cat: 'Comércio',
    preco: 'A partir de R$ 50,00',
    desc: 'Venda de mangueiras, ferramentas de jardim, adubos e acessórios para irrigação. Ideal para cuidar do seu quintal.',
    tags: ['jardim', 'irrigação', 'plantas'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 97777-5555',
    badge: '',
  },
  {
    id: 4,
    titulo: 'FixaTudo Ferragens',
    cat: 'Comércio',
    preco: 'A partir de R$ 20,00',
    desc: 'Parafusos, grampos, ferramentas e acessórios para manutenção e montagem. Produtos novos e seminovos.',
    tags: ['ferragens', 'bancada', 'manutenção'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 96666-7777',
    badge: 'Usado',
  },
  {
    id: 5,
    titulo: 'Livraria Técnica Campinas',
    cat: 'Comércio',
    preco: 'A partir de R$ 30,00',
    desc: 'Livros técnicos de elétrica, construção e manutenção. Ideal para estudantes e profissionais da área.',
    tags: ['livro', 'elétrica', 'técnico'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 95555-2222',
    badge: '',
  },
  {
    id: 6,
    titulo: 'Serviços Rápidos Nova Europa',
    cat: 'Serviços',
    preco: 'A partir de R$ 80/h',
    desc: 'Serviços de marido de aluguel: elétrica, hidráulica, pintura e montagem de móveis. Atendimento rápido no bairro.',
    tags: ['reparos', 'pintura', 'hidráulica'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 94444-3333',
    badge: '',
  },
  {
    id: 7,
    titulo: 'Padaria Nova Europa',
    cat: 'Comércio',
    preco: 'A partir de R$ 5,00',
    desc: 'Pães frescos, bolos, salgados e café da manhã completo. Atendimento rápido e ambiente familiar.',
    tags: ['padaria', 'café', 'pães'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 93333-1111',
    badge: 'Popular',
  },
  {
    id: 8,
    titulo: 'Mercado Boa Compra',
    cat: 'Comércio',
    preco: 'Consulte no local',
    desc: 'Mercado de bairro com hortifruti fresco, açougue e mercearia completa. Entregas na região.',
    tags: ['mercado', 'alimentos', 'delivery'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 92222-2222',
    badge: '',
  },
  {
    id: 9,
    titulo: 'Auto Elétrica Nova Europa',
    cat: 'Serviços',
    preco: 'A partir de R$ 100,00',
    desc: 'Serviços elétricos automotivos, bateria, alternador e diagnóstico completo.',
    tags: ['carro', 'elétrica', 'automotivo'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 91111-3333',
    badge: '',
  },
  {
    id: 10,
    titulo: 'Salão Beleza & Estilo',
    cat: 'Serviços',
    preco: 'A partir de R$ 30,00',
    desc: 'Cortes, escova, coloração e tratamentos capilares. Atendimento com hora marcada.',
    tags: ['beleza', 'cabelo', 'salão'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 94444-1111',
    badge: '',
  },
  {
    id: 11,
    titulo: 'Pet Shop Amigo Fiel',
    cat: 'Comércio',
    preco: 'A partir de R$ 20,00',
    desc: 'Rações, acessórios e banho e tosa para seu pet. Atendimento com carinho e qualidade.',
    tags: ['pet', 'ração', 'banho'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 95555-3333',
    badge: '',
  },
  {
    id: 12,
    titulo: 'Farmácia Vida Mais',
    cat: 'Comércio',
    preco: 'Consulte no local',
    desc: 'Medicamentos, produtos de higiene e perfumaria. Atendimento rápido e preços acessíveis.',
    tags: ['farmácia', 'saúde', 'remédios'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 96666-1111',
    badge: '24h',
  },
  {
    id: 13,
    titulo: 'Lanchonete Sabor Caseiro',
    cat: 'Comércio',
    preco: 'A partir de R$ 15,00',
    desc: 'Lanches, porções e refeições rápidas com sabor de comida caseira.',
    tags: ['lanche', 'comida', 'rápido'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 97777-1111',
    badge: '',
  },
  {
    id: 14,
    titulo: 'Oficina Mecânica Nova Europa',
    cat: 'Serviços',
    preco: 'Sob consulta',
    desc: 'Manutenção geral, troca de óleo, freios e revisão completa para seu veículo.',
    tags: ['oficina', 'carro', 'manutenção'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 98888-1111',
    badge: '',
  },
  {
    id: 15,
    titulo: 'Loja de Roupas Estilo Urbano',
    cat: 'Comércio',
    preco: 'A partir de R$ 49,90',
    desc: 'Moda masculina e feminina com peças modernas e preços acessíveis.',
    tags: ['roupa', 'moda', 'estilo'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 99999-1111',
    badge: 'Novo',
  },
  {
    id: 16,
    titulo: 'Academia Nova Europa Fitness',
    cat: 'Serviços',
    preco: 'A partir de R$ 79,90/mês',
    desc: 'Academia completa com musculação, personal trainer e aulas funcionais.',
    tags: ['academia', 'fitness', 'saúde'],
    local: 'Jardim Nova Europa, Campinas/SP',
    contato: '(19) 90000-1111',
    badge: '',
  },
  {
  id: 17,
  titulo: 'Açougue Nova Europa',
  cat: 'Comércio',
  preco: 'Consulte no local',
  desc: 'Carnes frescas, cortes especiais e atendimento personalizado.',
  tags: ['açougue', 'carne', 'alimentos'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0001',
  badge: '',
},
{
  id: 18,
  titulo: 'Hortifruti Verde Vida',
  cat: 'Comércio',
  preco: 'A partir de R$ 3,00',
  desc: 'Frutas, verduras e legumes frescos direto do produtor.',
  tags: ['hortifruti', 'saudável', 'orgânico'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0002',
  badge: '',
},
{
  id: 19,
  titulo: 'Casa de Ração Animal Feliz',
  cat: 'Comércio',
  preco: 'A partir de R$ 25,00',
  desc: 'Rações e acessórios para cães, gatos e aves.',
  tags: ['pet', 'ração', 'animais'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0003',
  badge: '',
},
{
  id: 20,
  titulo: 'Papelaria Nova Europa',
  cat: 'Comércio',
  preco: 'A partir de R$ 2,00',
  desc: 'Material escolar, escritório e papelaria completa.',
  tags: ['papelaria', 'escola', 'escritório'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0004',
  badge: '',
},
{
  id: 21,
  titulo: 'Loja de Utilidades do Lar',
  cat: 'Comércio',
  preco: 'A partir de R$ 10,00',
  desc: 'Utensílios domésticos, cozinha e decoração.',
  tags: ['casa', 'utilidades', 'decoração'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0005',
  badge: '',
},
{
  id: 22,
  titulo: 'Sorveteria Doce Gelato',
  cat: 'Comércio',
  preco: 'A partir de R$ 8,00',
  desc: 'Sorvetes artesanais e açaí com diversos acompanhamentos.',
  tags: ['sorvete', 'açaí', 'doce'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0006',
  badge: 'Popular',
},
{
  id: 23,
  titulo: 'Chaveiro Rápido 24h',
  cat: 'Serviços',
  preco: 'Sob consulta',
  desc: 'Abertura de portas, cópia de chaves e atendimento emergencial.',
  tags: ['chaveiro', '24h', 'urgente'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0007',
  badge: '24h',
},
{
  id: 24,
  titulo: 'Lavanderia Lava Fácil',
  cat: 'Serviços',
  preco: 'A partir de R$ 15,00',
  desc: 'Lavagem e secagem de roupas com qualidade e rapidez.',
  tags: ['lavanderia', 'roupa', 'limpeza'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0008',
  badge: '',
},
{
  id: 25,
  titulo: 'Borracharia Nova Europa',
  cat: 'Serviços',
  preco: 'A partir de R$ 20,00',
  desc: 'Conserto e troca de pneus com atendimento rápido.',
  tags: ['pneu', 'carro', 'borracharia'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0009',
  badge: '',
},
{
  id: 26,
  titulo: 'Distribuidora de Bebidas Nova Europa',
  cat: 'Comércio',
  preco: 'A partir de R$ 5,00',
  desc: 'Bebidas em geral com entrega rápida no bairro.',
  tags: ['bebidas', 'delivery', 'festa'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0010',
  badge: '',
},
{
  id: 27,
  titulo: 'Loja de Celulares Conecta',
  cat: 'Comércio',
  preco: 'A partir de R$ 100,00',
  desc: 'Venda de celulares, acessórios e assistência técnica.',
  tags: ['celular', 'tecnologia', 'assistência'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0011',
  badge: '',
},
{
  id: 28,
  titulo: 'Gráfica Rápida Nova Europa',
  cat: 'Serviços',
  preco: 'Sob consulta',
  desc: 'Impressões, cartões de visita e serviços gráficos em geral.',
  tags: ['gráfica', 'impressão', 'design'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0012',
  badge: '',
},
{
  id: 29,
  titulo: 'Assistência Técnica EletroFix',
  cat: 'Serviços',
  preco: 'Sob consulta',
  desc: 'Conserto de eletrodomésticos e eletrônicos.',
  tags: ['assistência', 'eletrônicos', 'reparo'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0013',
  badge: '',
},
{
  id: 30,
  titulo: 'Floricultura Jardim & Amor',
  cat: 'Comércio',
  preco: 'A partir de R$ 20,00',
  desc: 'Flores, arranjos e presentes para todas as ocasiões.',
  tags: ['flores', 'presentes', 'decoração'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0014',
  badge: '',
},
{
  id: 31,
  titulo: 'Loja de Calçados Passo Firme',
  cat: 'Comércio',
  preco: 'A partir de R$ 79,90',
  desc: 'Calçados masculinos, femininos e infantis.',
  tags: ['calçados', 'sapatos', 'moda'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0015',
  badge: '',
},
{
  id: 32,
  titulo: 'Barbearia Estilo Fino',
  cat: 'Serviços',
  preco: 'A partir de R$ 25,00',
  desc: 'Cortes modernos, barba e atendimento diferenciado.',
  tags: ['barbearia', 'corte', 'estilo'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0016',
  badge: '',
},
{
  id: 33,
  titulo: 'Restaurante Sabor do Bairro',
  cat: 'Comércio',
  preco: 'A partir de R$ 20,00',
  desc: 'Almoço caseiro com marmitas e pratos feitos.',
  tags: ['restaurante', 'almoço', 'comida'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0017',
  badge: '',
},
{
  id: 34,
  titulo: 'Depósito de Gás Nova Europa',
  cat: 'Comércio',
  preco: 'Consulte no local',
  desc: 'Venda e entrega de gás de cozinha no bairro.',
  tags: ['gás', 'entrega', 'cozinha'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0018',
  badge: '',
},
{
  id: 35,
  titulo: 'Loja de Bicicletas Pedal Livre',
  cat: 'Comércio',
  preco: 'A partir de R$ 300,00',
  desc: 'Venda e manutenção de bicicletas e acessórios.',
  tags: ['bicicleta', 'esporte', 'manutenção'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0019',
  badge: '',
},
{
  id: 36,
  titulo: 'Studio Fotográfico Nova Europa',
  cat: 'Serviços',
  preco: 'Sob consulta',
  desc: 'Ensaios fotográficos, eventos e fotos profissionais.',
  tags: ['foto', 'evento', 'ensaio'],
  local: 'Jardim Nova Europa, Campinas/SP',
  contato: '(19) 91111-0020',
  badge: '',
}
]

let filtrado = [...dados]
let searchTerm = ''

function highlight(text, term) {
  if (!term) return text
  const re = new RegExp(
    `(${term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`,
    'gi'
  )
  return text.replace(re, '<mark>$1</mark>')
}

function renderGrid(items) {
  const grid = document.getElementById('grid')
  const label = document.getElementById('sectionLabel')
  label.textContent = searchTerm
    ? `${items.length} resultado${items.length !== 1 ? 's' : ''} para "${searchTerm}"`
    : 'Todos os anúncios'

  if (!items.length) {
    grid.innerHTML = `<div class="empty-state"><div class="big">🔍</div><p>Nenhum classificado encontrado para "<strong>${searchTerm}</strong>"</p></div>`
    return
  }

  grid.innerHTML = items
    .map(
      (d, i) => `
    <div class="card" style="animation-delay:${i * 0.06}s" onclick="openCard(${d.id})">
      ${d.badge ? `<span class="card-badge">${d.badge}</span>` : ''}
      <div class="card-category">${d.cat}</div>
      <div class="card-title">${highlight(d.titulo, searchTerm)}</div>
      <div class="card-desc">${highlight(d.desc.substring(0, 90) + '…', searchTerm)}</div>
      <div class="card-footer">
        <span class="card-price">${d.preco}</span>
        <span class="card-contact">📍 ${d.local.split(',')[0]}</span>
      </div>
    </div>
  `
    )
    .join('')
}

function doSearch() {
  searchTerm = document.getElementById('searchInput').value.trim()
  if (!searchTerm) {
    filtrado = [...dados]
  } else {
    const q = searchTerm.toLowerCase()
    filtrado = dados.filter(
      (d) =>
        d.titulo.toLowerCase().includes(q) ||
        d.desc.toLowerCase().includes(q) ||
        d.cat.toLowerCase().includes(q) ||
        d.tags.some((t) => t.toLowerCase().includes(q))
    )
  }
  renderGrid(filtrado)
}

document.getElementById('searchInput').addEventListener('input', doSearch)
document.getElementById('searchInput').addEventListener('keydown', (e) => {
  if (e.key === 'Enter') doSearch()
})

function openCard(id) {
  const d = dados.find((x) => x.id === id)
  if (!d) return
  document.getElementById('mCat').textContent = d.cat
  document.getElementById('mTitle').textContent = d.titulo
  document.getElementById('mPrice').textContent = d.preco
  document.getElementById('mDesc').textContent = d.desc
  document.getElementById('mTags').innerHTML = d.tags
    .map((t) => `<span class="tag">${t}</span>`)
    .join('')
  document.getElementById('mInfo').innerHTML = `
    <div class="info-item"><div class="info-label">Localização</div><div class="info-val">${d.local}</div></div>
    <div class="info-item"><div class="info-label">Contato</div><div class="info-val">${d.contato}</div></div>
    <div class="info-item"><div class="info-label">Categoria</div><div class="info-val">${d.cat}</div></div>
    <div class="info-item"><div class="info-label">Anúncio Nº</div><div class="info-val">#${String(d.id).padStart(4, '0')}</div></div>
  `
  document.getElementById('mContact').textContent = `Contatar: ${d.contato}`
  openOverlay('viewOverlay')
}

function openOverlay(id) {
  document.getElementById(id).classList.add('active')
}
function closeOverlay(id) {
  document.getElementById(id).classList.remove('active')
}

function closeViewModal(e) {
  if (e.target === document.getElementById('viewOverlay'))
    closeOverlay('viewOverlay')
}
function closeViewModal2(e) {
  if (e.target === document.getElementById('addOverlay'))
    closeOverlay('addOverlay')
}

function openAddModal() {
  openOverlay('addOverlay')
}

function addClassificado() {
  const titulo = document.getElementById('fTitle').value.trim()
  const cat = document.getElementById('fCat').value
  const preco = document.getElementById('fPrice').value
  const desc = document.getElementById('fDesc').value.trim()
  const contato = document.getElementById('fContact').value.trim()
  const local = document.getElementById('fLocal').value.trim()
  const tagsStr = document.getElementById('fTags').value.trim()

  if (!titulo || !desc) {
    alert('Preencha ao menos o título e a descrição.')
    return
  }

  const novoId = dados.length ? Math.max(...dados.map((d) => d.id)) + 1 : 1
  dados.unshift({
    id: novoId,
    titulo,
    cat,
    preco: preco
      ? `R$ ${parseFloat(preco).toFixed(2).replace('.', ',')}`
      : 'Sob consulta',
    desc,
    tags: tagsStr
      ? tagsStr
          .split(',')
          .map((t) => t.trim())
          .filter(Boolean)
      : [],
    local: local || 'Brasil',
    contato: contato || 'Não informado',
    badge: 'Novo',
  })

  // clear form
  ;['fTitle', 'fPrice', 'fDesc', 'fContact', 'fLocal', 'fTags'].forEach(
    (id) => (document.getElementById(id).value = '')
  )
  closeOverlay('addOverlay')
  searchTerm = ''
  document.getElementById('searchInput').value = ''
  filtrado = [...dados]
  renderGrid(filtrado)
}

renderGrid(dados)
