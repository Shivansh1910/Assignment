import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RegcComponent } from './regc.component';

describe('RegcComponent', () => {
  let component: RegcComponent;
  let fixture: ComponentFixture<RegcComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RegcComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(RegcComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
