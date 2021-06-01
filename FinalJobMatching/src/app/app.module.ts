import { CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { MatSliderModule } from '@angular/material/slider';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NavbarComponent } from './navbar/navbar.component';
import { MaterialModule } from './material/material.module';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import {  FormsModule} from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { JobsComponent } from './jobs/jobs.component';
import { AuthService } from './AuthService/auth.service';
import { JobService } from './JobService/job.service'
import { EmployeeLoginComponent } from './employee-login/employee-login.component';
import { HomeComponent } from './home/home.component';
import { SideNavComponent } from './side-nav/side-nav.component';



@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    LoginComponent,
    RegisterComponent,
    JobsComponent,
    EmployeeLoginComponent,
    HomeComponent,
    SideNavComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    MatSliderModule,
    MaterialModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [AuthService, JobService],
  bootstrap: [AppComponent],
  schemas: [
    CUSTOM_ELEMENTS_SCHEMA
  ]
})
export class AppModule { }
