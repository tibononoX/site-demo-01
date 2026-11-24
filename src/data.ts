// Contenus repris du site actuel de FV Peinture (fvpeinture.ch) et du cahier des charges. Ne rien inventer.
import villa from './assets/img/fv/villa-founex.jpg';
import arcade1 from './assets/img/fv/arcade-facade-1.jpg';
import arcade9 from './assets/img/fv/arcade-facade-9.jpg';
import app1 from './assets/img/fv/appartement-1.jpg';
import app2 from './assets/img/fv/appartement-2.jpg';
export const SERVICES = [
  { t: 'Peinture intérieure', s: 'Murs, plafonds, décoration', c: 'c1', slug: 'peinture-interieure' },
  { t: 'Extérieur & façades', s: 'Isolation périphérique', c: 'c2', slug: 'peinture-exterieure-facades' },
  { t: 'Plâtrerie', s: 'Plafonds, murs intérieurs et extérieurs', c: 'c3', slug: 'platrerie-cloisons' },
  { t: 'Cloisons', s: 'Placo-plâtre, carreaux plâtre', c: 'c4', slug: 'platrerie-cloisons' },
  { t: 'Sols résine & carrelage', s: 'Résine polyuréthane / époxyde', c: 'c5', slug: 'sols-resine-carrelage' },
  { t: 'Film solaire UV', s: 'Fenêtres, véranda, pergola', c: 'c6', slug: 'film-solaire-uv' },
];
export const ENG = [
  ['Un seul interlocuteur', 'Franck Viollier, votre contact direct.'],
  ['Suivi quotidien', 'Nous vous tenons informé de l’évolution des travaux.'],
  ['Propre et ponctuel', 'Propreté des travaux, qualité de la finition, respect des délais.'],
  ['Matériaux suisses', 'Matériaux suisses de haute qualité, collaborateurs diplômés en Suisse.'],
];
export const PROJECTS = [
  { id: 'arcade', t: 'Arcade professionnelle', where: 'Genève', d: 'Rénovation de la façade du magasin « graphic store » avec peinture minérale.', p: 'Façade, peinture extérieure', imgs: [arcade1, arcade9] },
  { id: 'appartement', t: 'Appartement 3,5 pièces', where: 'Genève', d: 'Rénovation complète d’un appartement de 3,5 pièces.', p: 'Plâtres, peintures, sols ; cloisons légères en placo-plâtre', imgs: [app1, app2] },
  { id: 'villa', t: 'Villa mitoyenne', where: 'Founex', d: 'Rafraîchissement complet des murs et des plafonds d’une villa mitoyenne.', p: 'Peinture murs et plafonds', imgs: [villa] },
];
export const TRADES = [
  { t: 'Peinture intérieure', slug: 'peinture-interieure', d: 'Tous travaux de peinture intérieurs ainsi que travaux de décoration, crépissage, tapisserie, émail, vernis, laque, giclage.', c: 'c1', img: villa, cap: 'Villa mitoyenne, Founex' },
  { t: 'Peinture extérieure & façades', slug: 'peinture-exterieure-facades', d: 'Tous travaux de peinture extérieurs : avant-toits, dispersion sur façades, crépi, ciment, béton, chaux, portes, fenêtres, volets, fer forgé, portails, barrières, garages, corniches, traçage de route. Isolation périphérique en façade avec crépi de finition, exécution avec divers types d’isolation.', c: 'c2', img: arcade9, cap: 'Arcade professionnelle, Genève' },
  { t: 'Plâtrerie & cloisons', slug: 'platrerie-cloisons', d: 'Enduisage divers, plafonds, murs intérieurs et extérieurs. Cloisons légères en placo-plâtre avec châssis métallique, cloisons en carreaux de plâtre.', c: 'c3', img: app1, cap: 'Appartement 3,5 pièces, Genève' },
  { t: 'Sols résine & carrelage', slug: 'sols-resine-carrelage', d: 'Peinture de sol en résine à deux composants polyuréthane / époxyde, et carrelage.', c: 'c5', img: app2, cap: 'Appartement 3,5 pièces, Genève' },
  { t: 'Film solaire UV', slug: 'film-solaire-uv', d: 'Pose de film solaire UV pour vos fenêtres, véranda, pergola ou abri de piscine.', c: 'c6' },
];
export const STEPS = [
  ['Devis', 'Vous nous présentez votre projet, nous établissons votre devis.'],
  ['Chantier', 'Un seul interlocuteur et un suivi quotidien de l’avancement des travaux.'],
  ['Finitions', 'La qualité des finitions, la propreté et le respect des délais.'],
];
