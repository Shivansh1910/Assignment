import { Component, OnInit, OnDestroy, HostListener } from "@angular/core";
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: "app-registerpage",
  templateUrl: "registerpage.component.html"
})
export class RegisterpageComponent implements OnInit, OnDestroy {
  isCollapsed = true;
  focus;
  focus1;
  focus2;
  name;
  // namem;
  email;
  // emailm;
  username;
  // usernamem;
  password;
  // passwordm;

  constructor(private http: HttpClient, private router: Router) { }

  @HostListener("document:mousemove", ["$event"])
  onMouseMove(e) {
    var squares1 = document.getElementById("square1");
    var squares2 = document.getElementById("square2");
    var squares3 = document.getElementById("square3");
    var squares4 = document.getElementById("square4");
    var squares5 = document.getElementById("square5");
    var squares6 = document.getElementById("square6");
    var squares7 = document.getElementById("square7");
    var squares8 = document.getElementById("square8");

    var posX = e.clientX - window.innerWidth / 2;
    var posY = e.clientY - window.innerWidth / 6;

    squares1.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.05 +
      "deg) rotateX(" +
      posY * -0.05 +
      "deg)";
    squares2.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.05 +
      "deg) rotateX(" +
      posY * -0.05 +
      "deg)";
    squares3.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.05 +
      "deg) rotateX(" +
      posY * -0.05 +
      "deg)";
    squares4.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.05 +
      "deg) rotateX(" +
      posY * -0.05 +
      "deg)";
    squares5.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.05 +
      "deg) rotateX(" +
      posY * -0.05 +
      "deg)";
    squares6.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.05 +
      "deg) rotateX(" +
      posY * -0.05 +
      "deg)";
    squares7.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.02 +
      "deg) rotateX(" +
      posY * -0.02 +
      "deg)";
    squares8.style.transform =
      "perspective(500px) rotateY(" +
      posX * 0.02 +
      "deg) rotateX(" +
      posY * -0.02 +
      "deg)";
  }

  ngOnInit() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.add("register-page");

    this.onMouseMove(event);
  }
  ngOnDestroy() {
    var body = document.getElementsByTagName("body")[0];
    body.classList.remove("register-page");
  }

  submit() {
    console.log(this.name, this.email, this.username, this.password)
    var url = "http://127.0.0.1:8000/portal/regc/";
    var body = new FormData();
    body.append('name', this.name)
    body.append('email', this.email)
    body.append('username', this.username)
    body.append('password', this.password)

    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
        localStorage.setItem('hp_token', data['token'])
        this.router.navigateByUrl('/login')
      }
    )

  };

  submitm() {
    console.log(this.name, this.email, this.username, this.password)
    var url = "http://127.0.0.1:8000/portal/regm/";
    var body = new FormData();
    body.append('name', this.name)
    body.append('email', this.email)
    body.append('username', this.username)
    body.append('password', this.password)

    this.http.post<any>(url, body).subscribe(
      data => {
        console.log(data)
        localStorage.setItem('hp_token', data['token'])
        this.router.navigateByUrl('/login')
      }
    )

  };
}
