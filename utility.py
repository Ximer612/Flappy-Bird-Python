def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def box_collides(firstX,firstY,secondX,secondY,firstHalfWidth,secondHalfWidth,firstHalfHeight,secondHalfHeight):
            distX = secondX - firstX
            distY = secondY - firstY

            deltaX = abs(distX) - (secondHalfWidth + firstHalfWidth)

            # No Horizontal Collision
            if deltaX > 0 :
                return False

            deltaY = abs(distY) - (firstHalfHeight + secondHalfHeight)

            # No Vertical Collision
            if deltaY > 0 :
                return False
                
            return True,-deltaX,-deltaY

def delta_collision(deltaX,deltaY,firstX,firstY,secondX,secondY):
            if deltaX < deltaY :                
                # Horizontal Collision
                if firstX < secondX :
                    deltaX = -deltaX
                firstX += deltaX
            else:
                # Vertical Collision
                if firstY < secondY:
                    deltaY = -deltaY
                else:
                    pass

                firstY += deltaY

            return firstX,firstY
            