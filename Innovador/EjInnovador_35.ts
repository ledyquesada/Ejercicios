//Enrutamiento avanzado

// Configuración de Rutas
const routes: Routes = [
  { path: 'items', component: ItemsListComponent },
  {
    path: 'items/:id',
    component: ItemDetailsComponent,
    children: [
      { path: 'details', component: ItemDetailsViewComponent },
      { path: 'comments', component: ItemCommentsComponent },
    ],
  },
];
