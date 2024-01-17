//
// Servicio de Datos
//

// data.service.ts
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  obtenerDatos() {
    // Simulación de obtención de datos de una API
    return ['Dato 1', 'Dato 2', 'Dato 3'];
  }
}


// data.component.ts
import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-data',
  template: `
    <h2>Datos obtenidos:</h2>
    <ul>
      <li *ngFor="let dato of datos">{{ dato }}</li>
    </ul>
  `,
})
export class DataComponent implements OnInit {
  datos: string[] = [];

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.datos = this.dataService.obtenerDatos();
  }
}
