//
//Directiva personalizada
//

// resaltar.directive.ts
import { Directive, ElementRef, HostListener } from '@angular/core';

@Directive({
  selector: '[appResaltar]',
})
export class ResaltarDirective {
  constructor(private el: ElementRef) {}

  @HostListener('mouseenter') onMouseEnter() {
    this.cambiarColorFondo('amarillo');
  }

  @HostListener('mouseleave') onMouseLeave() {
    this.cambiarColorFondo('');
  }

  private cambiarColorFondo(color: string) {
    this.el.nativeElement.style.backgroundColor = color;
  }
}
