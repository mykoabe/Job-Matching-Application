import { Component } from '@angular/core';
import { RestService } from './Services/rest.service';
import { Works } from './works';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  title = 'FinalJobMatching';
  
  constructor(private rs : RestService){}

  headers = ["id","jobtype", "availability",  "status"]

  work : Works[] = [];

  ngOnInit()
  {
      this.rs.readWorks()
      .subscribe
        (
          (response) => 
          {
            this.work = response[0]["data"];
          },
          (error) =>
          {
            console.log("No Data Found" + error);
          }

        )
  }
}
