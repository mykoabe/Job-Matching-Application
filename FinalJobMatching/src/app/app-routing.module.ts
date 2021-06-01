import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { EmployeeLoginComponent } from './employee-login/employee-login.component';
import { HomeComponent } from './home/home.component';
import { JobsComponent } from './jobs/jobs.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';

const routes: Routes =[
  {path: '', redirectTo: 'home', pathMatch: 'full'},
  {path: "login", component: LoginComponent},
  {path: "home", component: HomeComponent},
  {path: "register", component: RegisterComponent},
  {path: "jobs", component: JobsComponent},
  {path: "employeeLogin", component: EmployeeLoginComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
