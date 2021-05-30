import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { JobsComponent } from './jobs/jobs.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes =[
  {path: '', redirectTo: 'register', pathMatch: 'full'},
  {path: "login", component: LoginComponent},
  {path: "register", component: RegisterComponent},
  {path: "jobs", component: JobsComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
