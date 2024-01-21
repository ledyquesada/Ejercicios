//Animaciones en Angular

// Configuración de Animaciones
@Component({
  selector: 'app-fade-in',
  template: `<div [@fadeIn]="animationState">Contenido</div>`,
  animations: [
    trigger('fadeIn', [
      transition(':enter', [
        style({ opacity: 0 }),
        animate('300ms', style({ opacity: 1 })),
      ]),
    ]),
  ],
})
export class FadeInComponent {
  animationState = 'in';
}
