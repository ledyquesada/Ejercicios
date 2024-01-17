//
// Rutas
//

// app-routing.module.ts
import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { InicioComponent } from './inicio.component';
import { DetalleComponent } from './detalle.component';

const routes: Routes = [
  { path: 'inicio', component: InicioComponent },
  { path: 'detalle', component: DetalleComponent },
  { path: '', redirectTo: '/inicio', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {}


// inicio.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-inicio',
  template: '<p>Componente de Inicio</p><a routerLink="/detalle">Ir a Detalle</a>',
})
export class InicioComponent {}



// detalle.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-detalle',
  template: '<p>Componente de Detalle</p>',
})
export class DetalleComponent {}
