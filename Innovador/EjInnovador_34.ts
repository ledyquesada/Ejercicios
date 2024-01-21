//Uso de componentes

// Componente
export class CompletedTasksComponent implements OnInit {
  completedTasks$ = this.store.pipe(select(selectCompletedTasks));

  constructor(private store: Store) {}

  ngOnInit(): void {
    this.store.dispatch(loadTasks()); // Disparar la carga de tareas al inicializar el componente
  }
}
