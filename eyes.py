class eyeWindow:
    def __init__(self):
        import turtle

        self.wn = turtle.Screen()
        self.wn.bgcolor("black")
        self.wn.setup(width = 1.0, height = 1.0)
        turtle.tracer(0)

        self.eye_turtles = {
        "left_white": turtle.Turtle(),
        "right_white": turtle.Turtle(),
        "left_iris": turtle.Turtle(),
        "right_iris": turtle.Turtle(),
        "left_pupil": turtle.Turtle(),
        "right_pupil": turtle.Turtle(),
        "left_pupil_highlight": turtle.Turtle(),
        "right_pupil_highlight": turtle.Turtle(),
        }

        # left_pupil.color("black")
        # right_pupil.color("black")
        self.pupils = (self.eye_turtles["left_pupil"], self.eye_turtles["right_pupil"])
        self.irises = (self.eye_turtles["left_iris"], self.eye_turtles["right_iris"])
        self.whites = (self.eye_turtles["left_white"], self.eye_turtles["right_white"])
        self.pupil_highlights = (self.eye_turtles["left_pupil_highlight"], self.eye_turtles["right_pupil_highlight"])

        self.left_eye_turtle_pos = (-200, 0)
        self.right_eye_turtle_pos = (200, 0)
        self.left_pupil_highlight_pos = (-214, 14)
        self.right_pupil_highlight_pos = (186, 14)

        for pupil in self.pupils:
            pupil.color("black")
            pupil.shapesize(2, 2)

        for iris in self.irises:
            iris.color("blue")
            iris.shapesize(4, 4)

        for white in self.whites:
            white.color("white")
            white.shapesize(6, 12)

        for pupil_highlight in self.pupil_highlights:
            pupil_highlight.color("white")
            pupil_highlight.shapesize(0.6, 0.6)

        def setup_turtle(turtle):
            turtle.penup()
            turtle.speed(0)
            turtle.shape("circle")

        for eye_turtle_key in self.eye_turtles.keys():
            eye_turtle = self.eye_turtles[eye_turtle_key]
            setup_turtle(eye_turtle)

            if eye_turtle_key.endswith("pupil_highlight"):
                if eye_turtle_key.startswith("left"):
                    eye_turtle.goto(self.left_pupil_highlight_pos[0], self.left_pupil_highlight_pos[1])
                elif eye_turtle_key.startswith("right"):
                    eye_turtle.goto(self.right_pupil_highlight_pos[0], self.right_pupil_highlight_pos[1])

            elif eye_turtle_key.startswith("left"):
                eye_turtle.goto(self.left_eye_turtle_pos[0], self.left_eye_turtle_pos[1])

            elif eye_turtle_key.startswith("right"):
                eye_turtle.goto(self.right_eye_turtle_pos[0], self.right_eye_turtle_pos[1])

        self.wn.update()

        def move_eyes(pos):
            if type(pos) != list:
                raise TypeError("`pos` must be a list.")
            if abs(pos[0]) > 30:
                pos[0] = pos[0]/abs(pos[0])*30
            if abs(pos[1]) > 15:
                pos[1] = pos[1]/abs(pos[1])*15
            for eye_turtle_key in self.eye_turtles.keys():
                eye_turtle = self.eye_turtles[eye_turtle_key]
                if not eye_turtle_key.endswith("white"):
                    if eye_turtle_key.endswith("pupil_highlight"):
                            if eye_turtle_key.startswith("left"):
                                eye_turtle.goto(self.left_pupil_highlight_pos[0] + pos[0], self.left_pupil_highlight_pos[1] + pos[1])

                            elif eye_turtle_key.startswith("right"):
                                eye_turtle.goto(self.right_pupil_highlight_pos[0]  + pos[0], self.right_pupil_highlight_pos[1]  + pos[1])
                    
                    elif eye_turtle_key.startswith("left"):
                        eye_turtle.goto(self.left_eye_turtle_pos[0] + pos[0], self.left_eye_turtle_pos[1] + pos[1])
                
                    elif eye_turtle_key.startswith("right"):
                        eye_turtle.goto(self.right_eye_turtle_pos[0] + pos[0], self.right_eye_turtle_pos[1] + pos[1])
        
        self.move_eyes = move_eyes
        
        self.wn.update()
        #remove close, min, and max buttons:
        # canvas = self.wn.getcanvas()
        # root = canvas.winfo_toplevel()
        # root.overrideredirect(1) # type: ignore

    def update(self):
        self.wn.update()
