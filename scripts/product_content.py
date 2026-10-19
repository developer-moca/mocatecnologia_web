"""Public product information. Sources are listed in README.md."""
PRODUCTS = {
 'dungeon-fighters': {
  'name':'Dungeon Fighters',
  'image':'https://dungeonfighters.github.io/Web/assets/images/screenshot-0.png',
  'tag':('Jogo · Ação','Game · Action'),
  'intro':('Enfrente ondas de monstros, sobreviva às arenas e jogue com amigos em um hack and slash da Moca.','Battle waves of monsters, survive the arenas and play with friends in a hack and slash from Moca.'),
  'heading':('Uma arena. Muitos inimigos.','One arena. Countless enemies.'),
  'body':('Dungeon Fighters combina combate em arenas com ondas de inimigos e desafios de sobrevivência. Monstros com lanças, explosivos, flechas e machados exigem movimento e atenção a cada confronto.','Dungeon Fighters combines arena combat with waves of enemies and survival challenges. Monsters wielding spears, explosives, arrows and axes demand movement and attention in every encounter.'),
  'features':[
   (('Solo ou acompanhado','Solo or together'),('Jogue sozinho ou reúna até quatro jogadores no multiplayer local, com modos cooperativo e versus.','Play solo or bring together up to four players in local multiplayer, with cooperative and versus modes.')),
   (('Combate e sobrevivência','Combat and survival'),('Enfrente inimigos com diferentes armas e encontre espaço para sobreviver em meio ao combate.','Face enemies with different weapons and find room to survive in the midst of combat.')),
   (('Novos desafios','New challenges'),('Conquiste estrelas de desempenho e desbloqueie novos níveis.','Earn performance stars and unlock new levels.'))],
  'links':[(('Visitar o site do jogo','Visit the game website'),'https://dungeonfighters.github.io/Web/')],
  'gallery':[(f'https://dungeonfighters.github.io/Web/assets/images/screenshot-{i}.png',('Cena de combate em Dungeon Fighters','Combat scene in Dungeon Fighters')) for i in [1,2,3]],
 },
 'tooda': {
  'name':'TOODA — Safe Children','image':'/images/clients/moca-tooda-cover.png',
  'tag':('Solução · Proteção e cuidado','Solution · Protection and care'),
  'intro':('Pulseiras de identificação e tecnologia para apoiar a proteção de pessoas vulneráveis em praias e eventos.','Identification wristbands and technology to support the protection of vulnerable people at beaches and events.'),
  'heading':('Tecnologia a serviço do cuidado.','Technology that cares.'),
  'body':('O projeto TOODA — Safe Children busca apoiar a segurança de pessoas vulneráveis em ambientes de praia. A Moca contribui com o desenvolvimento tecnológico da solução. Em 2026, a FIA-RJ firmou uma parceria com a TOODA para utilizar as pulseiras no Carnaval. As apresentações mostram a proposta e a participação técnica da Moca.','TOODA — Safe Children aims to support the safety of vulnerable people in beach environments. Moca contributes to the technological development of the solution. In 2026, FIA-RJ partnered with TOODA to use its wristbands during Carnival. The presentations explain the proposal and Moca’s technical participation.'),
  'features':[
   (('O contexto','The context'),('Proteção e auxílio na localização de pessoas nas praias do Rio de Janeiro.','Protection and help locating people on Rio de Janeiro’s beaches.')),
   (('A solução','The solution'),('Conheça a proposta de Safe Children na apresentação do projeto.','Explore the Safe Children proposal in the project presentation.')),
   (('A contribuição da Moca','Moca’s contribution'),('Consulte a apresentação técnica para conhecer a abordagem de desenvolvimento e as tecnologias utilizadas.','See the technical presentation for the development approach and technologies used.'))],
  'links':[(('Apresentação da solução (PDF)','Solution presentation (PDF)'),'/files/tooda-pitch.pdf'),(('Apresentação técnica (PDF)','Technical presentation (PDF)'),'/files/moca-tooda-project.pdf')],
  'gallery':[],
 },
 'paper-hero': {
  'name':'Paper Hero','image':'https://i.ytimg.com/vi/pX-UymX0gXg/hqdefault.jpg',
  'tag':('Jogo · Moca','Game · Moca'),
  'intro':('Conheça Paper Hero em movimento no vídeo de apresentação do jogo.','Discover Paper Hero in action in the game’s presentation video.'),
  'heading':('Conheça o jogo em ação.','See the game in action.'),
  'body':('Paper Hero faz parte dos jogos da Moca. O vídeo de apresentação é o ponto de partida para conhecer seu universo visual e acompanhar uma amostra da experiência.','Paper Hero is part of Moca’s games portfolio. Its presentation video offers an introduction to its visual world and a glimpse of the experience.'),
  'features':[],
  'links':[(('Assistir à apresentação','Watch the presentation'),'https://www.youtube.com/watch?v=pX-UymX0gXg')],
  'video':'https://www.youtube-nocookie.com/embed/pX-UymX0gXg',
  'gallery':[],
 },
 'kalimour': {
  'name':'Kalimour','image':'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2402460/header.jpg?t=1707143301',
  'tag':('Jogo · Estratégia e construção','Game · Strategy and city building'),
  'intro':('Construa cidades, explore territórios e desenvolva seu reino em um jogo de estratégia em hexágonos.','Build cities, explore new lands and grow your kingdom in a hex-based strategy game.'),
  'heading':('Um reino para construir. Um mundo para explorar.','A kingdom to build. A world to explore.'),
  'body':('Em Kalimour, você desenvolve um domínio em terras hostis, expande suas fronteiras e enfrenta animais selvagens, bandidos e reinos rivais. A construção de cidades se encontra com a gestão de recursos e o combate tático.','In Kalimour, you develop a domain in hostile lands, expand your borders and face wild animals, bandits and rival kingdoms. City building meets resource management and tactical combat.'),
  'features':[
   (('Explore e construa','Explore and build'),('Encontre recursos e expanda a infraestrutura dos seus assentamentos.','Find resources and expand your settlements’ infrastructure.')),
   (('Desenvolva a economia','Grow your economy'),('Agricultura, caça e mineração ajudam a sustentar o crescimento do reino.','Farming, hunting and mining help sustain your kingdom’s growth.')),
   (('Planeje sua estratégia','Plan your strategy'),('Treine tropas e adapte seu exército aos diferentes inimigos.','Train troops and adapt your army to different enemies.'))],
  'links':[(('Conheça na Steam','Explore on Steam'),'https://store.steampowered.com/app/2402460/Kalimour/')],
  'note':('Consulte a Steam para informações atuais sobre demo, lançamento e requisitos do sistema.','Visit Steam for current demo, release and system requirement information.'),
  'gallery':[],
 }
}
