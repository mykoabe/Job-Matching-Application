import { Component, OnInit } from '@angular/core';
import { RestService } from '../Services/rest.service';
import { Works } from '../works';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  title = 'FinalJobMatching';
  
  constructor(private rs : RestService){}

  headers = ["id","jobtype", "avaliabilty",  "status"]

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
