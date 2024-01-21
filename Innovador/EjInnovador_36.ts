//Formularios reactivos

// Ejemplo de Formulario Reactivo
this.profileForm = this.fb.group({
  username: ['', Validators.required],
  email: ['', [Validators.required, Validators.email]],
  password: ['', [Validators.required, Validators.minLength(8)]],
  confirmPassword: ['', [Validators.required, confirmPasswordValidator('password')]],
});
