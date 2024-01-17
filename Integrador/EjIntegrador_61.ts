//
// Componente dinámico
//

// dynamic.component.ts
import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-dynamic',
  template: `
    <div *ngIf="contentType === 'texto'">Este es un mensaje de texto.</div>
    <img *ngIf="contentType === 'imagen'" src="ruta/de/la/imagen.jpg" alt="Imagen de ejemplo" />
  `,
})
export class DynamicComponent {
  @Input() contentType: string = '';
}
